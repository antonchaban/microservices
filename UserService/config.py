"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    CSRF_ENABLED = True
    SECRET_KEY = 'you-will-never-guess'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

"""
from dotenv import load_dotenv

load_dotenv()

import os

user = os.environ.get("POSTGRES_USER")
password = os.environ.get("POSTGRES_PASSWORD")
server = os.environ.get("POSTGRES_HOST")
database = os.environ.get("POSTGRES_DB")
port = os.environ.get("POSTGRES_PORT")


class Config:
    DEBUG = True
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{password}' \
                              f'@{server}:{port}/{database}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
