from flask import current_app as _app
from flask_restful import Api as _Api
from flask_restful import Resource

from common.errors import _handle_error


class Api(_Api):
    """This class overrides 'handle_error' method of 'Api' class ,
    to extend global exception handing functionality of 'flask-restful'.
    """

    def handle_error(self, err):
        err_msg = getattr(err, "orig", err)
        _app.logger.error(f"{type(err)}: {err_msg}")  # log all errors in app
        return _handle_error(err)


class ApiResource(Resource):
    pass
