from flask_restful import Resource, marshal_with
from flask import abort, request
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
import bcrypt

from app import api, db, docs
from app.models import Users
from app.rest.constants import UserResponseSchema, PostUserRequestSchema, PutUserRequestSchema


class GetUser(MethodResource, Resource):
    @marshal_with(UserResponseSchema)
    def get(self, id):
        user = Users.query.get(id)

        if not user:
            abort(404)

        return user

    @use_kwargs(PutUserRequestSchema, location='query')
    @marshal_with(UserResponseSchema)
    def put(self, id, **kwargs):
        user = Users.query.get(id)

        username = kwargs.get('username', None)
        if username:
            user.username = username

        password = kwargs.get('password', None)
        if password:
            hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(rounds=10, prefix=b'2a'))
            hashed = "{bcrypt}" + hashed.decode()
            user.password = hashed

        db.session.commit()

        return user

    @marshal_with(UserResponseSchema)
    def delete(self, id):
        user = Users.query.get(id)

        if not user:
            abort(404)

        db.session.delete(user)
        db.session.commit()

        return user


class GetUsers(MethodResource, Resource):
    @marshal_with(UserResponseSchema(many=True))
    def get(self):
        users = Users.query.all()
        return users

    @use_kwargs(PostUserRequestSchema, location='query')
    @marshal_with(UserResponseSchema)
    def post(self, **kwargs):
        user = Users()

        for atr, value in kwargs.items():
            if atr == "password":
                hashed = bcrypt.hashpw(value.encode('utf-8'), bcrypt.gensalt(rounds=10, prefix=b'2a'))
                hashed = "{bcrypt}" + hashed.decode()
                setattr(user, atr, hashed)
            else:
                setattr(user, atr, value)

        db.session.add(user)
        db.session.commit()

        return user


api.add_resource(GetUsers, '/api/user/users')
api.add_resource(GetUser, '/api/user/users/<int:id>')

docs.register(GetUsers)
docs.register(GetUser)
