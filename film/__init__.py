from flask import Flask
#import pymysql
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)
from .models import *
from .models2 import *

def create_app():
    app = Flask(__name__)
    app.debug = True

    #app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:chis1chang@127.0.0.1:3306/movie?charset=utf8"
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:chis1chang@127.0.0.1:3306/movie?charset=utf8"
    app.config['SQLALCHEMY_BINDS'] = {
        'artcms': 'mysql+pymysql://root:chis1chang@127.0.0.1:3306/artcms?charset=utf8',
        #'movie':"mysql+pymysql://root:chis1chang@127.0.0.1:3306/movie?charset=utf8",
    }
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

    app.config["SECRET_KEY"] = "12345678"
    import os
    app.config["uploads"] = os.path.join(os.path.dirname(__file__), "static","uploads")

    return app




