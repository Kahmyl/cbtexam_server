from flask import Blueprint, jsonify, request


from .models import Admin

admin = Blueprint('admin', __name__)


@admin.route('/admin/register', methods=['GET', 'POST'])
def create_admin():
    if request.method == "POST":
        pass


