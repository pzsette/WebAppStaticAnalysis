from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("username", db.String(30), nullable=False)
    surname = db.Column("username", db.String(30), nullable=False)
    email = db.Column("email", db.String(100), nullable=False)
    password = db.Column("password", db.String(192), nullable=False)
    amount = db.Column("amount", db.Integer, nullable=False)
    filename = db.Column("filename", db.String, nullable=False)

    def __init__(self, name, surname, email, password, filename):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.amount = 0
        self.filename = filename
