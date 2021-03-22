from flask import current_app as _app
from flask import render_template_string
from flask_restful import Api as _Api
from flask_restful import Resource
from gfm import SemiSaneListExtension
from markdown import markdown
from mdx_gfm import GithubFlavoredMarkdownExtension

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


def init_index(app):
    @app.route("/")
    def index():
        with open("README.md", "r") as readme_file:
            html = markdown(
                readme_file.read(),
                extensions=[GithubFlavoredMarkdownExtension(), SemiSaneListExtension()],
            )
        return render_template_string(html)
