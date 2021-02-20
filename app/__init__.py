from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

def create_app():

    from app import auth, home, idcard

    with app.app_context():
        app.register_blueprint(auth.bp)
        app.register_blueprint(home.bp)
        app.register_blueprint(idcard.bp)
    with app.app_context():
        db.create_all()

    return app

