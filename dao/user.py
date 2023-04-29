from database.db import db


# Create the table user
class User(db.Model):
    __table_name__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False, unique=True)
    date_of_birth = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(100), nullable=True, unique=True)
    password = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(200), nullable=False)

    def __init__(self, user_id, name, surname, username, date_of_birth,
                 email, phone, password, image):
        self.id = user_id
        self.name = name
        self.surname = surname
        self.username = username
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone = phone
        self.password = password
        self.image = image
