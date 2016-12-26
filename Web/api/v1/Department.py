#! usr/bin/python
# -*- coding: utf-8 -*-

from flask import jsonify
from flask_restful import Api, Resource, url_for
import json


class Departments(Resource):
    def get(self, id):
        dict = {}
        dict["dept"] = u"IT部"
        return jsonify(dict)
