import os
from datetime import datetime, timedelta


import jwt

from cbtexam import db


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def encode_auth_token(self, admin_id):
        # Generates auth token for user
        try:
            payload = {
                'exp': datetime.utcnow() + timedelta(hours=1),
                'iat': datetime.utcnow(),
                'sub': admin_id
            }
            return jwt.encode(payload, os.environ.get('SECRET_KEY'), algorithm='HS256')

        except:
            pass

    @staticmethod
    def decode_auth_token(auth_token):
        # Decodes auth token returns integer or string
        try:
            payload = jwt.decode(auth_token, os.environ.get('SECRET_KEY'))
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
