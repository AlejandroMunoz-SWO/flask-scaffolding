from dao.role import Role
from database.db import db


# Get the role name by the id
def get_role_name(role_id):
    role = Role.query.filter_by(id=role_id).one_or_none()
    return role.name
