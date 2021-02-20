from flask_sqlalchemy import SQLAlchemy
from app import db


class CRUD:

    @staticmethod
    def add(resource):
        db.session.add(resource)
        return db.session.commit()

    @staticmethod
    def update(self):
        return db.session.commit()

    @staticmethod
    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()


class User(db.Model, CRUD):
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("username", db.String(30), nullable=False)
    surname = db.Column("surname", db.String(30), nullable=False)
    email = db.Column("email", db.String(100), nullable=False)
    password = db.Column("password", db.String(100), nullable=False)
    amount = db.Column("amount", db.Integer, nullable=False)
    filename = db.Column("filename", db.String(100), nullable=False)

    def __init__(self, name, surname, email, password, filename):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.amount = 0
        self.filename = filename
