from flask_marshmallow import Marshmallow

ma = Marshmallow()


# This is the schema for the User class
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'surname', 'username', 'date_of_birth', 'email', 'phone', 'password', 'image')
