from flask import Blueprint, make_response, render_template

from common.resources import Api, ApiResource

auth_bp = Blueprint("auth_bp", __name__, template_folder="templates")
api = Api(auth_bp)


class LoginApi(ApiResource):
    def get(self):
        return make_response(
            render_template("login.html"),
            200,
            {"Content-Type": "text/html"},
        )


class LogoutApi(ApiResource):
    def get(self):
        return make_response(
            render_template("logout.html"),
            200,
            {"Content-Type": "text/html"},
        )


api.add_resource(LoginApi, "/login")
api.add_resource(LogoutApi, "/logout")
