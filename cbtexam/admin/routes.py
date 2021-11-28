from flask import Blueprint, jsonify, request

from cbtexam import bcrypt, db


from .models import Admin

admin = Blueprint('admin', __name__)


@admin.route('/admin/register', methods=['GET', 'POST'])
def create_admin():
    if request.method == "POST" and request.is_json:
        data = request.get_json()
        admin = Admin.query.filter_by(username=data.get('username')).first()
        if not admin:
            hashed_password = bcrypt.generate_password_hash(
                data.get('password')).decode('utf-8')
            admin = Admin(username=data.get('username'),
                          password=hashed_password)
            db.session.add(admin)
            db.session.commit()
            return jsonify({"message": "Admin account has been created successfully"})
    else:
        return jsonify({"error": "The request payload is not in JSON format"})


@admin.route('/admin/login/', methods=['POST'])
def login():
    if request.method == "POST" and request.is_json:
        data = request.get_json()
        try:
            admin = Admin.query.filter_by(
                username=data.get('username')).first()
            if admin and bcrypt.check_password_hash(admin.password, data.get('password')):
                auth_token = admin.encode_auth_token(admin.id)

                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'auth_token': auth_token.decode()
                    }
                    return jsonify(response_object), 200

        except Exception as e:
            response_object = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.'
            }
            return jsonify(response_object), 500


def get_user():
    auth_header = request.headers.get('Authorization')
    if auth_header:
        auth_token = auth_header.split(" ")[1]
    else:
        auth_token = ''
    if auth_token:
        resp = Admin.decode_auth_token(auth_token)
        if not isinstance(resp, str):
            admin = Admin.query.filter_by(id=resp).first()
            response_object = {
                'status': 'success',
                'data': {
                    'user_id': admin.id,
                    'username': admin.username,
                }
            }
            return jsonify(response_object), 200

        response_object = {
            'status': 'fail',
            'message': resp
        }
        return jsonify(response_object), 500
    else:
        response_object = {
            'status': 'fail',
            'message': 'Provide a valid auth token.'
        }
        return jsonify(response_object), 500
