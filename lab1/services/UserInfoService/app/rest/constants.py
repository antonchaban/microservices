from flask_restful import reqparse, fields

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

url_resource = {
    'id': fields.Integer,
    'code': fields.String,
    'url': fields.String,
    'user_id': fields.Integer,
    'expires_stamp': fields.String,
    'created_stamp': fields.String,
    'user_name': fields.String
}

user_resource = {
    'id': fields.Integer,
    'username': fields.String,
    'password': fields.String,
    'created_stamp': fields.String,
    'get_links': fields.Nested(url_resource)
}
