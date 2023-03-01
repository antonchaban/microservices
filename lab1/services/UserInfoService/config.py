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

user = os.environ.get('DBL_USER')
password = os.environ.get('DB_PASSWORD')
server = os.environ.get('DB_HOST')
database = os.environ.get('DB_NAME')


class Config:
    DEBUG = True
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{password}' \
                              f'@{server}/{database}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
"""
