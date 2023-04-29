from flask_marshmallow import Marshmallow

ma = Marshmallow()


# This is the schema for the Role class
class RoleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')
