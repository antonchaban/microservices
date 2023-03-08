from flask_restful import Resource, marshal_with
from flask_apispec.views import MethodResource

from app import api, db, docs

class GetHealth(MethodResource, Resource):
    def get(self):
        return None, 200

api.add_resource(GetHealth, '/api/user/health')

docs.register(GetHealth)
