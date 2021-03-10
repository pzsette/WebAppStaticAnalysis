from app import create_app
from database import db

app = create_app()
db.init_app(app)
reveal_type(db)
reveal_type(db.connection)
reveal_type(db.connection.cursor)

if __name__ == '__main__':

    app.run(debug=app.config['DEBUG'])
