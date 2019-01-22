from flask import Flask
#import pymysql
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from .models import *

def create_app():
    app = Flask(__name__)
    app.debug = True

    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:chis1chang@127.0.0.1:3306/movie?charset=utf8"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_POOL_SIZE'] = 10
    app.config['SQLALCHEMY_MAX_OVERFLOW'] = 5
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True

    from film.home import home as home_blueprint
    from film.admin import admin as admin_blueprint
    app.register_blueprint(home_blueprint)
    app.register_blueprint(admin_blueprint,url_prefix='/admin')
    db.init_app(app)

    return app




