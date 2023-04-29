from sqlalchemy import CheckConstraint
from database.db import db


# Create the table role
class Role(db.Model):
    __table_name__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, default='student')

    valid_roles = ['admin', 'student', 'professor']
    __table_args__ = (CheckConstraint(name.in_(valid_roles)), {})

    def __init__(self, role_id, name):
        self.id = role_id
        self.name = name
