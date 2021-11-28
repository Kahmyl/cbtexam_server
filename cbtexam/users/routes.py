from flask import Blueprint, render_template
from flask_bcrypt import Bcrypt
from flask import request, jsonify
from cbtexam import app, db
from cbtexam.users.models import UsersModel
from flask_login import login_user, current_user, logout_user, login_required

users = Blueprint('users', __name__)
bcrypt = Bcrypt()

@users.route('/users')
def hello():
    return "Hello"


@users.route("/register", methods=['POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()
        user = UsersModel.query.filter_by(email=data['email']).first()
        if user:
            return "Email already exists"
        else:
            hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
            new_user = UsersModel(name=data['name'], email=data['email'], password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            return {"message": f"user {new_user.name} has been registered successfully."}

@users.route("/login", methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        user = UsersModel.query.filter_by(email=data['email']).first()
        if user and bcrypt.check_password_hash(user.password, data['password']):
            return {"message": f"user {user.name} is logged in."}




        
