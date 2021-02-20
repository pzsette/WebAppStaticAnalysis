from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


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


class Action(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    id_user = db.Column("id_user", db.Integer, nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now, nullable=False)
    amount = db.Column("amount", db.Integer)
    causal = db.Column("causal", db.String(150))
    operationType = db.Column("type", db.Enum("deposit", "withdraw"))

    def __init__(self, id_user, amount, causal, operationType):
        self.id_user = id_user,
        self.amount = amount,
        self.causal = causal,
        self.operationType = operationType
