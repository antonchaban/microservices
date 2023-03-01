from flask_restful import Resource, marshal_with
from flask import abort, request

from app import api, db
from app.models import Links
from app.rest.constants import url_resource, url_args


class GetUrl(Resource):
    @marshal_with(url_resource)
    def get(self, id):
        url = Links.query.get(id)

        if not url:
            abort(404)

        return url

    @marshal_with(url_resource)
    def delete(self, id):
        url = Links.query.get(id)

        if not url:
            abort(404)

        db.session.delete(url)
        db.session.commit()

        return url

    @marshal_with(url_resource)
    def put(self, id):
        link = Links.query.get(id)

        args = url_args.parse_args()

        code = args.get('code', None)
        if code:
            link.code = code

        url = args.get('url', None)
        if url:
            link.url = url

        user_id = args.get('user_id', None)
        if user_id:
            link.user_id = user_id

        expires_stamp = args.get('expires_stamp', None)
        if expires_stamp:
            link.expires_stamp = expires_stamp

        db.session.commit()

        return link


class GetUrls(Resource):
    @marshal_with(url_resource)
    def get(self):
        urls = Links.query.all()
        return urls

    @marshal_with(url_resource)
    def post(self):
        url = Links()

        for atr, value in url_args.parse_args().items():
            setattr(url, atr, value)

        db.session.add(url)
        db.session.commit()

        return url


api.add_resource(GetUrl, '/json_urls/<int:id>')
api.add_resource(GetUrls, '/json_urls')

