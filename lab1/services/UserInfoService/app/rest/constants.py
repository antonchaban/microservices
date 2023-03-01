from flask_restful import reqparse, fields

user_resource = {
    'id': fields.Integer,
    'code': fields.String,
    'url': fields.String,
    'user_id': fields.Integer,
    'expiration_stamp': fields.String,
    'created_stamp': fields.String
}
