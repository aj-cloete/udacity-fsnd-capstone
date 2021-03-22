"""Error/Exception classes"""
from flask import jsonify as _jsonify
from flask_restful import HTTPException as _HTTPException
from sqlalchemy.exc import SQLAlchemyError as _SQLAlchemyError
from werkzeug.http import HTTP_STATUS_CODES as _HTTP_STATUS_CODES


class Error(_HTTPException):
    message = "Generic Exception"
    code = 500


def _handle_error(err):
    """It helps preventing writing unnecessary
    try/except block though out the application
    """
    # Handle HTTPExceptions
    if isinstance(err, _HTTPException):
        msg = getattr(err, "description", _HTTP_STATUS_CODES.get(err.code, ""))
        msg = msg if msg else getattr(err, "message", "unspecified")
        return (
            _jsonify(
                {
                    "message": msg,
                    "status_code": err.code,
                    "details": str(err),
                }
            ),
            err.code,
        )

    # Handle SQLAlchemyErrors
    if isinstance(err, _SQLAlchemyError):
        return (
            _jsonify(
                {
                    "message": "Backend error encountered.",
                    "details": str(getattr(err, "orig", err)).split("\n")[0],
                    "status_code": 400,
                }
            ),
            400,
        )

    # If message attribute is not set,
    # consider it as Python core exception and
    # hide sensitive error info from end user
    if not getattr(err, "message", None):
        return (
            _jsonify(
                {
                    "message": "Server has encountered an error",
                    "status_code": 500,
                    "details": "Python error.  See server logs for details",
                }
            ),
            500,
        )
    # Handle application specific custom exceptions
    return _jsonify(**err.kwargs), err.http_status_code
