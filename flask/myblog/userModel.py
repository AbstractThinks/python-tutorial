# -*- coding: utf-8 -*-

from myblog import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    # def is_authenticated(self):
    #     return True
    #
    # def is_active(self):
    #     return True
    #
    # def is_anonymous(self):
    #     return False
    #
    # def get_id(self):
    #     return str(self.id)
    #
    # #装饰器
    # @classmethod
    # def login_check(cls, user_name):
    #     user = cls.query.filter(db.or_(User.nickname == user_name, User.email == user_name)).first()
    #
    #     if not user:
    #         return None
    #
    #     return user


    def __repr__(self):
        return '<User %r>' %(self.nickname)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    body = db.Column(db.String(140))
