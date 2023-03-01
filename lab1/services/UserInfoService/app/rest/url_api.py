from flask_restful import Resource, marshal_with
from flask import abort, request

from app import api, db, docs
from app.models import Links
from app.rest.constants import UrlResponseSchema, PostUrlRequestSchema, PutUrlRequestSchema

from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource


class GetUrl(MethodResource, Resource):
    @marshal_with(UrlResponseSchema)
    def get(self, id):
        url = Links.query.get(id)

        if not url:
            abort(404)

        return url

    @marshal_with(UrlResponseSchema)
    def delete(self, id):
        url = Links.query.get(id)

        if not url:
            abort(404)

        db.session.delete(url)
        db.session.commit()

        return url

    @use_kwargs(PutUrlRequestSchema, location='query')
    @marshal_with(UrlResponseSchema)
    def put(self, id, **kwargs):
        link = Links.query.get(id)

        code = kwargs.get('code', None)
        if code:
            link.code = code

        url = kwargs.get('url', None)
        if url:
            link.url = url

        user_id = kwargs.get('user_id', None)
        if user_id:
            link.user_id = user_id

        expires_stamp = kwargs.get('expires_stamp', None)
        if expires_stamp:
            link.expires_stamp = expires_stamp

        db.session.commit()

        return link


class GetUrls(MethodResource, Resource):
    @marshal_with(UrlResponseSchema(many=True))
    def get(self):
        urls = Links.query.all()
        return urls

    @use_kwargs(PostUrlRequestSchema, location='query')
    @marshal_with(UrlResponseSchema)
    def post(self, **kwargs):
        url = Links()

        for atr, value in kwargs.items():
            setattr(url, atr, value)

        db.session.add(url)
        db.session.commit()

        return url


api.add_resource(GetUrl, '/json_urls/<int:id>')
api.add_resource(GetUrls, '/json_urls')

docs.register(GetUrls)
docs.register(GetUrl)

