from flask import Flask, g, redirect
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
import hashlib
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/AMS"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = 60 * 60 * 30

db = SQLAlchemy(app)

app.secret_key = hashlib.new("md5", os.urandom(24)).hexdigest()


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print('login_required')
        try:
            if g.user_id is None:
                return redirect("/account/login")
        except Exception as ex:
            print(ex)
        return f(*args, **kwargs)

    return decorated_function


from .controls import Home, User

app.register_blueprint(Home, url_prefix='/')
app.register_blueprint(Home, url_prefix='/home')
app.register_blueprint(User, url_prefix='/user')

from .api.v1 import blueprint

app.register_blueprint(blueprint, url_prefix='/api/v1')

# app.register_blueprint(account, url_prefix='/account')


# @app.before_request
# def before_request():
#     try:
#         if request.url.find("/static") < 0:
#             if request.url.find("/account/login") > 0:
#                 pass
#             else:
#                 if "user_id" in session:
#                     g.user_id = session["user_id"]
#                     g.user_name = session["user_name"]
#                 else:
#                     return redirect("/account/login")
#
#     except Exception, ex:
#         print ex
