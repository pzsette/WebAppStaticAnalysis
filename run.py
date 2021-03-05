from app import create_app
from database import db
from flask_mysqldb import MySQL

app = create_app()
db = MySQL(app)

if __name__ == '__main__':

    app.run(debug=app.config['DEBUG'])
