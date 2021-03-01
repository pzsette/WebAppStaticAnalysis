from flask import Flask
app = Flask(__name__)
app.config.from_object('config')


def create_app():
    from app import auth, home, idcard

    with app.app_context():
        app.register_blueprint(auth.bp)
        app.register_blueprint(home.bp)
        app.register_blueprint(idcard.bp)

    return app

