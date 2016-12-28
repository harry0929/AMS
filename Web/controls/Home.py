#! usr/bin/python
# coding=utf-8
import operator
from flask import Blueprint, render_template
from Web.services import MenuService

Home = Blueprint('Home', __name__, template_folder='templates', static_url_path='', static_folder='')


@Home.route('/', methods=('GET', "POST"))
@Home.route('/index', methods=('GET', "POST"))
def index():
    return render_template("Home/index.html")


@Home.route('/getMenus', methods=('GET', "POST"))
def get_menus():
    menu = MenuService()
    return menu.get_menus_to_json()


@Home.route('/mainpage', methods=('GET', "POST"))
def mainpage():
    return "首页"
