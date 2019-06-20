from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from .config import config_by_name

import os

db = SQLAlchemy()
flask_bcrypt = Bcrypt()


def create_app(config_name):
    template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    template_dir = os.path.join(template_dir, 'templates')
    app = Flask(__name__, template_folder=template_dir)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)

    return app
