from flask import Blueprint, jsonify

admin = Blueprint('admin', __name__)

@admin.route('/admin/register', methods=['GET', 'POST'])
def create_admin():
    pass