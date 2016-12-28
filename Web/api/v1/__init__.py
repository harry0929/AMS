#! usr/bin/python
# -*- coding: utf-8 -*-

from .Asset import Assets, AssetsList
from .Department import Departments

from flask import Blueprint
from flask_restful import Api

blueprint = Blueprint('Asset', __name__, template_folder='templates', static_url_path='', static_folder='')

api = Api()

api.init_app(blueprint)

api.add_resource(Assets, '/Asset/<string:code>')
api.add_resource(AssetsList, '/Assets')
api.add_resource(Departments, '/Departments/<string:id>')
