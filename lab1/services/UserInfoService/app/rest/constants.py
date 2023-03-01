from flask_restful import reqparse, fields
from marshmallow import Schema, fields


url_args = reqparse.RequestParser()

url_args.add_argument('code', type=str, location='args')
url_args.add_argument('url', type=str, location='args')
url_args.add_argument('user_id', type=int, location='args')
url_args.add_argument('expires_stamp', type=str, location='args')
url_args.add_argument('created_stamp', type=str, location='args')
user_args = reqparse.RequestParser()

user_args.add_argument('username', type=str, location='args')
user_args.add_argument('password', type=str, location='args')
user_args.add_argument('created_stamp', type=str, location='args')


class UrlResponseSchema(Schema):
    id = fields.Integer()
    code = fields.String()
    url = fields.String()
    user_id = fields.Integer()
    expires_stamp = fields.String()
    created_stamp = fields.String()
    user_name = fields.String()


class PostUrlRequestSchema(Schema):
    code = fields.String(required=True)
    url = fields.String(required=True)
    user_id = fields.Integer(required=True)
    expires_stamp = fields.String()
    created_stamp = fields.String()


class PutUrlRequestSchema(Schema):
    code = fields.String()
    url = fields.String()
    user_id = fields.Integer()
    expires_stamp = fields.String()


class UserResponseSchema(Schema):
    id = fields.Integer()
    username = fields.String()
    password = fields.String()
    created_stamp = fields.String()
    links = fields.Nested(UrlResponseSchema(many=True))


class PostUserRequestSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)
    created_stamp = fields.String()


class PutUserRequestSchema(Schema):
    username = fields.String()
    password = fields.String()
    created_stamp = fields.String()



