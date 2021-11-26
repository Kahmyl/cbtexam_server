from flask import Flask


from cbtexam.users.routes import users
from .config import Config



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)


    from cbtexam.users.routes import users

    app.register_blueprint(users)   


    return app

