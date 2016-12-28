#! usr/bin/python
# coding=utf-8
from flask import jsonify, request
from flask_restful import Resource
from Web.models import Asset
from Web import db


class Assets(Resource):
    def get(self, code):
        m = Asset.query.filter(Asset.code == str(code)).first()
        if m is not None:
            return jsonify(code=0, result="ok", data=m.to_dict())
        else:
            return jsonify(code=-1, result="无记录", data="")

    def put(self, code):
        pass

    def delete(self, code):
        pass


class AssetsList(Resource):
    def get(self):

        count = int(request.args.get("c", 100))
        page = int(request.args.get("p", 0))
        models = Asset.query.limit(count).offset(count * page).all()
        arr = []
        if len(models) > 0:
            for m in models:
                arr.append(m.to_dict())
            return jsonify(code=0, result="ok", data=arr)
        else:
            return jsonify(code=-1, result="无记录", data="")

    def post(self):

        if "code" in request.args:
            pass

        try:
            asset = Asset()
            asset.code = 1

        except Exception as ex:
            return jsonify(code=0, result=ex, data="")
