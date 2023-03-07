from marshmallow import Schema, fields


class UserResponseSchema(Schema):
    id = fields.Integer()
    username = fields.String()


class PostUserRequestSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)


class PutUserRequestSchema(Schema):
    username = fields.String()
    password = fields.String()

