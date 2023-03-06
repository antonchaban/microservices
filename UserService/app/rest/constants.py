from flask_restful import reqparse, fields
from marshmallow import Schema, fields

user_args = reqparse.RequestParser()
user_args.add_argument('username', type=str, location='args')
user_args.add_argument('password', type=str, location='args')

class UserResponseSchema(Schema):
    id = fields.Integer()
    username = fields.String()

class PostUserRequestSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)

class PutUserRequestSchema(Schema):
    username = fields.String()
    password = fields.String()

