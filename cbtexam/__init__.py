from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from cbtexam.users.routes import users
from .config import Config

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)


    from cbtexam.users.routes import users

    app.register_blueprint(users)   


    return app

