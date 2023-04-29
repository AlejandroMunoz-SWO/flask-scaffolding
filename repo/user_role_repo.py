from dao.user_role import UserRole
from repo.role_repo import get_role_name
from database.db import db


# Get user roles by user id
def get_user_roles(user_id):
    user_roles = UserRole.query.filter_by(user_id=user_id).all()
    roles = []
    for user_role in user_roles:
        roles.append(get_role_name(user_role.role_id))
    return roles
