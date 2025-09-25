from flask_restx import Resource

from configs import dify_config
from controllers.service_api import service_api_ns


@service_api_ns.route("/")
class IndexApi(Resource):
    @service_api_ns.doc("get_service_api_index")
    @service_api_ns.doc(description="Retrieve basic metadata about the Service API entrypoint.")
    @service_api_ns.doc(
        responses={
            200: "Service API root information retrieved successfully",
        }
    )
    def get(self):
        """Return Service API root metadata."""

        return {
            "welcome": "Dify OpenAPI",
            "api_version": "v1",
            "server_version": dify_config.project.version,
        }
