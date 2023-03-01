from app import db
from sqlalchemy.sql import func


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    created_stamp = db.Column(db.DateTime)

    def __repr__(self):
        return f'{self.user_name}'


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String, unique=True, nullable=False)
    url = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    expiration_stamp = db.Column(db.DateTime(timezone=True), server_default=None)
    created_stamp = db.Column(db.DateTime(timezone=True), server_default=func.now())


"""
create table LINKS
(
    id            serial primary key,
    code          varchar not null unique,
    url           varchar not null,
    user_id       integer not null references USERS (id),
    expires_stamp timestamp default null,
    created_stamp timestamp default current_timestamp
);
"""
