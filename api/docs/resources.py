from flask import Blueprint, make_response, render_template_string

from common.resources import Api, ApiResource

docs_bp = Blueprint("docs_bp", __name__)
api = Api(docs_bp)


class DocApi(ApiResource):
    def get(self):
        return make_response(
            render_template_string(self.render_markdown("README.md")),
            200,
            {"Content-Type": "text/html"},
        )


class APIApi(ApiResource):
    def get(self):
        return make_response(
            render_template_string(self.render_markdown("API.md")),
            200,
            {"Content-Type": "text/html"},
        )


api.add_resource(APIApi, "/", "/API.md")
api.add_resource(DocApi, "/README.md")
