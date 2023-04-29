from repo.user_repo import *
from schemas.user_schema import *
from flask import request, jsonify
from werkzeug.security import generate_password_hash

user_schema = UserSchema()
users_schema = UserSchema(many=True)


# Update password
def update_password_controller(user_id):
    password = request.json['password']
    password = generate_password_hash(password)
    user_by_request = User(None, None, None, None, None, None, None, password, None)
    return user_schema.jsonify(update_password_repo(user_by_request, user_id))


# Login admin
def login_admin_controller():
    username = request.json['username']
    password = request.json['password']
    return admin_login_repo(username, password)

