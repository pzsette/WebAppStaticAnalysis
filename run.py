from app import create_app
import database
from flask_mysqldb import MySQL

app = create_app()
database.db = MySQL(app)
if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
