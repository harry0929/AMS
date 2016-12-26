#! usr/bin/python
# coding=utf-8
from flask import jsonify
from flask_restful import Resource
from Web.models import Asset


class Assets(Resource):

    def get(self, code):
        m = Asset.query.filter(Asset.code == code).first()
        if m is not None:
            param = dict()
            param["id"] = m.id
            param["code"] = m.code
            param["name"] = m.name
            param["supplier_name"] = None if m.supplier is None else m.supplier.name
            param["manager_type"] = m.manager_type.name
            param["asset_category"] = m.asset_category.name
            param["purchase_date"] = m.purchase_date.strftime('%Y-%m-%d')
            param["original_value"] = str(m.original_value)
            param["depreciation_year"] = m.depreciation_year
            param["department_name"] = m.department.name
            param["position"] = m.position
            param["remark"] = m.remark
            return jsonify(code=0, result="ok", data=m)
        else:
            return jsonify(code=-1, result="false", data="")


