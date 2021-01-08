from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    db = SQLAlchemy(app)

    from app import auth, home, idcard

    with app.app_context():
        app.register_blueprint(auth.bp)
        app.register_blueprint(home.bp)
        app.register_blueprint(idcard.bp)

    db.create_all()

    return app

