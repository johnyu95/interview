from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CsrfProtect
from config import config

bootstrap = Bootstrap()
csrf = CsrfProtect()
db = SQLAlchemy()
moment = Moment()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)
    csrf.init_app(app)
    moment.init_app(app)

    from .main import main as main
    app.register_blueprint(main)

    return app
