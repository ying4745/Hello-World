# -*- coding: utf-8 -*-
from blog2 import db
from flask_login import UserMixin


class User(db.Model,UserMixin):
    __tablename__ = 'b_user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True)
    password = db.Column(db.String(16))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):  #测试用
        return '<User %r>' % self.username
