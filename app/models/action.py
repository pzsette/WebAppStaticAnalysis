import datetime
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


class Action(db.Model, CRUD):
    id = db.Column("id", db.Integer, primary_key=True)
    id_user = db.Column("id_user", db.Integer, nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now, nullable=False)
    amount = db.Column("amount", db.Integer)
    causal = db.Column("causal", db.String(150))
    operation_type = db.Column("type", db.Enum("deposit", "withdraw"))

    def __init__(self, id_user, amount, causal, operation_type):
        self.id_user = id_user,
        self.amount = amount,
        self.causal = causal,
        self.operation_type = operation_type
