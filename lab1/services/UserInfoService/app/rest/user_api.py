from flask_restful import Resource, marshal_with
from flask import abort, request

from app import api, db
from app.models import Users
from app.rest.constants import user_resource


class GetUsers(Resource):
    @marshal_with(user_resource)
    def get(self):
        users = Users.query.all()
        return users


api.add_resource(GetUsers, '/json_users')
