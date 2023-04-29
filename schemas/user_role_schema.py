from flask_marshmallow import Marshmallow

ma = Marshmallow()


# This is the schema for the User_Role class, which is the association table between User and Role
class UserRoleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id', 'role_id')
