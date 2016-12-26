#!/usr/bin/python
# -*- coding:utf-8 -*-

from Web import db


class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(9), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False)

    supplier_id = db.Column(db.INTEGER, db.ForeignKey('supplier.id'))
    supplier = db.relationship('Supplier',
                               backref=db.backref('Assets', lazy='dynamic'))


    manager_type_id = db.Column(db.Integer, db.ForeignKey('manager_type.id'))
    manager_type = db.relationship('ManagerType',
                               backref=db.backref('Assets', lazy='dynamic'))


    asset_category_id = db.Column(db.INTEGER, db.ForeignKey('asset_category.id'))
    asset_category = db.relationship('AssetCategory',
                                   backref=db.backref('Assets', lazy='dynamic'))

    purchase_date = db.Column(db.Date, nullable=False)
    original_value = db.Column(db.DECIMAL(10, 2), nullable=False)
    depreciation_year = db.Column(db.INTEGER, nullable=False)
    department_id = db.Column(db.INTEGER, db.ForeignKey('department.id'))
    department = db.relationship('Department',
                                   backref=db.backref('Assets', lazy='dynamic'))

    position = db.Column(db.String(50))
    remark = db.Column(db.String(100))
