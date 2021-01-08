from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Action(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    id_user = db.Column("id_user", db.Integer, nullable=False)
    date = db.Column(db.DateTime(timezone=True), server_default=db.sql.func.now(), nullable=False)

