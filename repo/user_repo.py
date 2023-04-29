from dao.user import User
from database.db import db
from repo.user_role_repo import get_user_roles
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token
from flask import jsonify
import datetime


# Update password
def update_password_repo(user, user_id):
    user_by_id = User.query.filter_by(id=user_id).one_or_none()
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    user_by_id.password = generate_password_hash(user.password)
    user_by_id.password = user.password
    db.session.commit()
    return user_by_id


# Login admin
def admin_login_repo(username, password):
    user = User.query.filter_by(username=username).one_or_none()
    print(user.username, user.password)

    if user is None:
        user = User.query.filter_by(email=username).one_or_none()

    if user is not None and check_password_hash(user.password, password):
        # Now we have to check if the user is admin, so we have to check the table user_role
        roles = get_user_roles(user.id)
        if 'admin' in roles:
            payload = {
                'id': user.id,
                'username': user.username,
                'roles': roles
            }

            token_config = {
                'payload': payload,
                'expires_delta': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            }
            token = create_access_token(token_config)
            return jsonify({'authorized': True, 'token': token}), 200
        else:
            return jsonify({'authorized': False, 'message': 'You are not admin'}), 401
    else:
        print(username, password)
        return jsonify({'authorized': False, 'message': 'Wrong credentials'}), 401

