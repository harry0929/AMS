#!/usr/bin/python
# -*- coding:utf-8 -*-

from Web import db
from sqlalchemy.orm.properties import ColumnProperty, RelationshipProperty
from sqlalchemy.orm.attributes import InstrumentedAttribute


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

    def to_dict(self):
        param = dict()
        param["id"] = self.id
        param["code"] = self.code
        param["name"] = self.name
        param["supplier_name"] = None if self.supplier is None else self.supplier.name
        param["manager_type"] = self.manager_type.name
        param["asset_category"] = self.asset_category.name
        param["purchase_date"] = self.purchase_date.strftime('%Y-%m-%d')
        param["original_value"] = str(self.original_value)
        param["depreciation_year"] = self.depreciation_year
        param["department_name"] = self.department.name
        param["position"] = self.position
        param["remark"] = self.remark
        return param

    def validator(self, agrs):

        print(type(Asset.code.property))

        for k, v in Asset.__dict__.items():
            if isinstance(v, InstrumentedAttribute):
                print("%s is InstrumentedAttribute" % v)
                print(k)
                expr = v.property
                if isinstance(expr, ColumnProperty):
                    print("ColumnProperty")

                else:
                    print("RelationshipProperty")
                    # expr = Asset.code
                    # print(isinstance(expr, InstrumentedAttribute))
                    # print(expr.property)
                    # print(isinstance(expr.property, ColumnProperty))
                    # if hasattr(expr, 'type'):
                    #     return expr.type
                    # elif isinstance(expr, InstrumentedAttribute):
                    #     expr = expr.property
                    #     print(type(expr))
                    # if isinstance(expr, ColumnProperty):
                    #     print(type(expr))
                    #     return expr.columns[0].type
                    # elif isinstance(expr, RelationshipProperty):
                    #     return expr.mapper.class_
                    # raise TypeError("Couldn't inspect type.")
