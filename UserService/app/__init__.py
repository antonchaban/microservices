from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from flask_cors import CORS

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)

db = SQLAlchemy(app)
api = Api(app)

app.config.update({
    'APISPEC_SPEC': APISpec(
        title='User Info',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
})
docs = FlaskApiSpec(app)


from app import views, models, rest
