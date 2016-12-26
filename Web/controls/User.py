#! usr/bin/python
# coding=utf-8

from flask import Blueprint, render_template

User = Blueprint('User', __name__, template_folder='templates', static_url_path='', static_folder='')


@User.route('/', methods=('GET', "POST"))
@User.route('/index', methods=('GET', "POST"))
def index():
    return "用户"