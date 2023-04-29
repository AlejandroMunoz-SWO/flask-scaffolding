from database.db import db


# Create the table user_role to connect users with roles
class UserRole(db.Model):
    __table_name__ = 'user_role'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)

    user = db.relationship('User', backref='user_role')
    role = db.relationship('Role', backref='user_role')

    def __init__(self, user_role_id, user_id, role_id):
        self.id = user_role_id
        self.user_id = user_id
        self.role_id = role_id
