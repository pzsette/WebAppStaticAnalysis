from flask import Flask, redirect, url_for, session

from database import db
import auth
import home
import idcard

app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'MySecretKey$%&'
app.config['UPLOAD_FOLDER'] = "idcards"
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_PORT'] = 8889
app.config['MYSQL_DB'] = 'bank'

db.init_app(app)


app.register_blueprint(auth.bp)
app.register_blueprint(home.bp)
app.register_blueprint(idcard.bp)


@app.route('/')
def hello_world():
    if 'loggedin' in session:
        return redirect(url_for('home.home', surname=session['surname']))
    else:
        return redirect(url_for('auth.login'))


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
