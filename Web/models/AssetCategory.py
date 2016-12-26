#!/usr/bin/python
# -*- coding:utf-8 -*-

from Web import db


class AssetCategory(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(2), nullable=False)