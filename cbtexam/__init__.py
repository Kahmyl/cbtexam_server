from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://zxxthniianorkg:24a64bfa968a5e2850795395f5e5fa670479853454718b75a4760c6b427332ac@ec2-44-193-182-0.compute-1.amazonaws.com:5432/dfmsbbi4v4m2na'
db = SQLAlchemy(app)
db.init_app(app)

from cbtexam.users.routes import users

app.register_blueprint(users)

from cbtexam.users import routes


