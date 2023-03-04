from app import db
from sqlalchemy.sql import func


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    created_stamp = db.Column(db.DateTime)

    links = db.relationship(
        'Links',
        back_populates='users',
        cascade='all, delete'
    )

    @property
    def get_links(self):
        links = self.links
        return links

    def __repr__(self):
        return f'{self.username}'


class Links(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String, unique=True, nullable=False)
    url = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    expires_stamp = db.Column(db.DateTime(timezone=True), server_default=None)
    created_stamp = db.Column(db.DateTime(timezone=True), server_default=func.now())

    users = db.relationship(
        'Users',
        back_populates='links',
    )

    @property
    def user_name(self):
        user = Users.query.filter(Users.id == self.user_id).first()
        return f'{user.username}'

    def __repr__(self):
        return f'{self.code}'


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
