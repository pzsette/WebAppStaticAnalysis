from flask import Flask, render_template, request, session, redirect, url_for
from flask_mysqldb import MySQL
import re

app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'MySecretKey$%&'

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_PORT'] = 8889
app.config['MYSQL_DB'] = 'bank'
mysql = MySQL(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login', methods=['POST', 'GET'])
def login():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        # Output message if something goes wrong...
        # Create variables for easy access
        email = request.form['email']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM accounts WHERE email = %s AND password = %s', (email, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists in accounts table in out database
        if account:
            print(account)
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account[0]
            session['name'] = account[1]
            session['surname'] = account[2]
            session['email'] = account[4]
            # Redirect to home page
            print("successo")
            return render_template('home.html', msg=msg)
        else:
            print("solita merda")
            # Account doesnt exist or email/password incorrect
            msg = 'Incorrect email/password!'
    return render_template('login.html', msg=msg)


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    print("signup")
    # Output message if something goes wrong...
    msg = ''
    if request.method == 'POST' and 'name' in request.form and 'surname' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        name = request.form['name']
        surname = request.form['surname']
        password = request.form['password']
        email = request.form['email']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM accounts WHERE email = %s', (email,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not name or not surname or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO accounts (name,surname,email,password,amount) VALUES (%s, %s, %s, %s, 0)', (name, surname, email, password,))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('signup.html', msg=msg)

# http://localhost:5000/logout - this will be the logout page
@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('name', None)
    session.pop('surname', None)
    session.pop('email', None)
    # Redirect to login page
    return redirect(url_for('login'))


@app.route('/home')
def home():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor()
        cursor.execute(" SELECT amount FROM accounts WHERE name='Pietro' AND surname='Zarri' ")
        data = cursor.fetchall()[0][0]
        return render_template('home.html', amount=data)
    return redirect(url_for('login'))


@app.route('/deposit/<amount>/<actual_amount>', methods=['POST'])
def deposit(amount, actual_amount):
    if request.method == 'POST':
        cursor = mysql.connection.cursor()
        data = str(int(actual_amount) + int(amount))
        sql ="UPDATE accounts SET amount='"+data+"' WHERE name='PIETRO' "
        print(sql)
        cursor.execute(sql)
        mysql.connection.commit()
        print("executed")
    return "ok"


@app.route('/withdraw/<amount>/<actual_amount>')
def withdraw(amount, actual_amount):
    if request.method == 'POST':
        cursor = mysql.connection.cursor()
        data = str(int(actual_amount) - int(amount))
        sql ="UPDATE accounts SET amount ='"+ data +"' WHERE name='PIETRO' AND surname='ZARRI'"
        print(sql)
        cursor.execute(sql)
        mysql.connection.commit()
    return "ok"


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
