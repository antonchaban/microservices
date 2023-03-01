from flask_restful import Resource, marshal_with
from flask import abort, request

from app import api, db
from app.models import Users
from app.rest.constants import user_resource, user_args


class GetUser(Resource):
    @marshal_with(user_resource)
    def get(self, id):
        user = Users.query.get(id)

        if not user:
            abort(404)

        return user

    @marshal_with(user_resource)
    def put(self, id):
        user = Users.query.get(id)

        args = user_args.parse_args()

        code = args.get('username', None)
        if username:
            user.username = username

        password = args.get('password', None)
        if password:
            user.password = password

        created_stamp = args.get('created_stamp', None)
        if created_stamp:
            user.created_stamp = created_stamp

        db.session.commit()

        return user

    @marshal_with(user_resource)
    def delete(self, id):
        user = Users.query.get(id)

        if not user:
            abort(404)

        db.session.delete(user)
        db.session.commit()

        return user


class GetUsers(Resource):
    @marshal_with(user_resource)
    def get(self):
        users = Users.query.all()
        return users

    @marshal_with(user_resource)
    def post(self):
        user = Users()

        for atr, value in user_args.parse_args().items():
            setattr(user, atr, value)

        db.session.add(user)
        db.session.commit()

        return user


api.add_resource(GetUsers, '/json_users')
api.add_resource(GetUser, '/json_users/<int:id>')
