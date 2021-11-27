from flask import Flask
from flask_sqlalchemy import SQLAlchemy
<<<<<<< HEAD
from cbtexam.config import Config
=======

from cbtexam.users.routes import users
from .config import Config
>>>>>>> 758cb92f8ff2662099ae015a0e02fb903833f462

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    db.init_app(app)


    from cbtexam.users.routes import users

    app.register_blueprint(users)   


    return app
