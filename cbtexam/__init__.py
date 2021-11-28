from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


from .config import Config

db = SQLAlchemy()


bcrypt = Bcrypt()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'
    db.init_app(app)

    bcrypt.init_app(app)

    from cbtexam.users.routes import users
    from cbtexam.admin.routes import admin

    app.register_blueprint(users)
    app.register_blueprint(admin)

    from cbtexam.admin.models import Admin
    # with app.app_context():
    #     db.create_all()

    return app
