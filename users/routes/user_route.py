from flask import Blueprint
from flask_jwt_extended import jwt_required
from users.controller.user_controller import *


users_routes = Blueprint('users_routes', __name__)


# Update password
@users_routes.put("/user/update/<int:user_id>")
def update_password(user_id):
    return update_password_controller(user_id)


# Login admin
@users_routes.post("/admin")
def login_admin():
    return login_admin_controller()

