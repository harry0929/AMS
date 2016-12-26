#!/usr/bin/python
# -*- coding:utf-8 -*-

from Web import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False)
    nickname = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(40), nullable=False)
    reg_time = db.Column(db.DateTime)
    status = db.Column(db.SmallInteger, default=0)
    deleted = db.Column(db.Boolean, default=False)

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    def __str__(self):
        return self.name.encode('gbk')

    def __repr__(self):
        return "<%s>" % self
