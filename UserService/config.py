import os

user = 'smjydhpffefdgi'
password = '2ea7743e1fd242f0d1c8fd49b5b21d459f606e67de4316878fc80f62355ee047'
server = 'ec2-176-34-211-0.eu-west-1.compute.amazonaws.com'
database = 'd8ahak39q8951c'
port = '5432'


class Config:
    DEBUG = False
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{password}' \
                              f'@{server}:{port}/{database}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
