import json
import os
from functools import wraps
from urllib.parse import urlencode
from urllib.request import urlopen

from flask import request, url_for
from jose import jwt
from werkzeug.utils import redirect

AUTH0_DOMAIN = os.environ.get("AUTH0_DOMAIN", "dev-ly1s0q43.eu.auth0.com")
ALGORITHMS = ["RS256"]
AUTH0_AUDIENCE = os.environ.get("AUTH0_AUDIENCE", "https://udacity-fsnd.herokuapp.com/")
AUTH0_CALLBACK_URL = os.environ.get("AUTH0_CALLBACK_URL")
AUTH0_CLIENT_ID = os.environ.get("AUTH0_CLIENT_ID")
AUTH0_CLIENT_SECRET = os.environ.get("AUTH0_CLIENT_SECRET")
AUTH0_BASE_URL = os.environ.get("AUTH0_BASE_URL")


def register(oauth):
    auth0 = oauth.register(
        "auth0",
        client_id=AUTH0_CLIENT_ID,
        client_secret=AUTH0_CLIENT_SECRET,
        api_base_url=AUTH0_BASE_URL,
        access_token_url=AUTH0_BASE_URL + "/oauth/token",
        authorize_url=AUTH0_BASE_URL + "/authorize",
        client_kwargs={
            "scope": "openid profile email",
        },
    )
    return auth0


def register_login_logout(app, oauth):
    auth0 = register(oauth)

    @app.route("/login")
    def login():
        return auth0.authorize_redirect(redirect_uri=AUTH0_CALLBACK_URL)

    @app.route("/logout")
    def logout():
        # Redirect user to logout endpoint
        params = {
            "returnTo": url_for("login", _external=True),
            "client_id": AUTH0_CLIENT_ID,
        }
        return redirect(auth0.api_base_url + "/v2/logout?" + urlencode(params))


# # AuthError Exception
class AuthError(Exception):
    """
    AuthError Exception
    A standardized way to communicate auth failure modes
    """

    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


# # Auth Header
"""
Attempt to get the header from the request
Raise an AuthError if no header is present
Attempt to split bearer and the token
Raise an AuthError if the header is malformed
Return the token part of the header
"""


def get_token_auth_header():
    """Obtains the Access Token from the Authorization Header"""
    auth = request.headers.get("Authorization", None)
    if not auth:
        raise AuthError(
            {
                "code": "authorization_header_missing",
                "description": "Authorization header is expected.",
            },
            401,
        )

    parts = auth.split()
    if parts[0].lower() != "bearer":
        raise AuthError(
            {
                "code": "invalid_header",
                "description": 'Authorization header must start with "Bearer".',
            },
            401,
        )

    elif len(parts) == 1:
        raise AuthError(
            {"code": "invalid_header", "description": "Token not found."}, 401
        )

    elif len(parts) > 2:
        raise AuthError(
            {
                "code": "invalid_header",
                "description": "Authorization header must be bearer token.",
            },
            401,
        )

    token = parts[1]
    return token


def check_permissions(permission, payload):
    """
    Raise an AuthError if permissions are not included in the payload
    Raise an AuthError if the requested permission string is not in the payload permissions array
    return True otherwise
    """
    if "permissions" not in payload:
        raise AuthError(
            {
                "code": "invalid_claims",
                "description": "Permissions not included in JWT.",
            },
            400,
        )

    if permission not in payload["permissions"]:
        raise AuthError(
            {"code": "unauthorized", "description": "Permission not found."}, 403
        )
    return True


def verify_decode_jwt(token):
    """
    Check for an Auth0 token with key id (kid)
    Verify the token using Auth0 /.well-known/jwks.json
    Decode the payload from the token
    Validate the claims
    Return the decoded payload
    """
    jsonurl = urlopen(f"https://{AUTH0_DOMAIN}/.well-known/jwks.json")
    jwks = json.loads(jsonurl.read())
    unverified_header = jwt.get_unverified_header(token)
    rsa_key = {}
    if "kid" not in unverified_header:
        raise AuthError(
            {"code": "invalid_header", "description": "Authorization malformed."}, 401
        )

    for key in jwks["keys"]:
        if key["kid"] == unverified_header["kid"]:
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"],
            }
    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=AUTH0_AUDIENCE,
                issuer="https://" + AUTH0_DOMAIN + "/",
            )

            return payload

        except jwt.ExpiredSignatureError:
            raise AuthError(
                {"code": "token_expired", "description": "Token expired."}, 401
            )

        except jwt.JWTClaimsError:
            raise AuthError(
                {
                    "code": "invalid_claims",
                    "description": "Incorrect claims. Please, check the audience and issuer.",
                },
                401,
            )
        except Exception:
            raise AuthError(
                {
                    "code": "invalid_header",
                    "description": "Unable to parse authentication token.",
                },
                400,
            )
    raise AuthError(
        {
            "code": "invalid_header",
            "description": "Unable to find the appropriate key.",
        },
        400,
    )


def requires_auth(permission=""):
    """
    Use the get_token_auth_header method to get the token
    Use the verify_decode_jwt method to decode the jwt
    Use the check_permissions method validate claims and check the requested permission
    Return the decorator which passes the decoded payload to the decorated method
    """

    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            payload = verify_decode_jwt(token)
            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)

        return wrapper

    return requires_auth_decorator
