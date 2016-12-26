#! usr/bin/python
# coding=utf-8

from Web import db


class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    link = db.Column(db.String(100))
    url = db.Column(db.String(20), nullable=False)
    pid = db.Column(db.Integer, nullable=False, default=0)
    published = db.Column(db.Boolean, nullable=False, default=False)
    order = db.Column(db.Integer, default=0)
    locked = db.Column(db.Boolean, default=False)
    deleted = db.Column(db.Boolean, default=False)
    nodeCount = db.Column(db.Integer, default=0)

    def __init__(self, *args, **kwargs):
        super(Menu, self).__init__(*args, **kwargs)

    def __str__(self):
        return self.name.encode('gbk')

    def __repr__(self):
        return "<%s>" % self
