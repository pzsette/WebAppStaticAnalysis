import hashlib

from flask import session, render_template, Blueprint, redirect, url_for, current_app, request
from database import db
import re
import os

bp = Blueprint('auth', __name__, url_prefix='/auth')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


@bp.route('/signup', methods=['POST', 'GET'])
def signup():
    # Output message if something goes wrong...
    msg = ''
    if request.method == 'POST' and 'name' in request.form and 'surname' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        name = request.form['name']
        surname = request.form['surname']
        password = hashlib.sha256(request.form['password'].encode("utf8")).hexdigest()
        email = request.form['email']
        id_card = request.files['file']
        if id_card and allowed_file(id_card.filename):

            cursor = db.connection.cursor()

            query = "SELECT * FROM accounts WHERE email ='"+email+"'"
            cursor.execute(query)

            account = cursor.fetchone()

            # If account exists show error and validation checks
            if account:
                msg = 'Account already exists!'
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                msg = 'Invalid email address!'
            elif not name or not surname or not password or not email:
                msg = 'Please fill out the form!'
            else:
                #filename = secure_filename(id_card.filename)
                id_card.save(os.path.join(current_app.config['UPLOAD_FOLDER'], id_card.filename))
                
                # Account doesnt exists and the form data is valid, now insert new account into accounts table
                query = "INSERT INTO accounts (name, surname, email, filename, password, amount) VALUES ('"+name+"','"+surname+"','"+email+"','"+id_card.filename+"','"+password+"',0)"
                print(query)
                cursor.execute(query)
                db.connection.commit()

                msg = 'You have successfully registered!'
        else:
            msg = 'Only PNG/JPG/JPEG file are allowed'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('signup.html', msg=msg)


@bp.route('/login', methods=['POST', 'GET'])
def login():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = hashlib.sha256(request.form['password'].encode("utf8")).hexdigest()
        cursor = db.connection.cursor()

        # TEXT TO LOGIN WITH SQL INJECTION: xxx@xxx' OR 1 = 1 LIMIT 1 -- '
        query = "SELECT * FROM accounts WHERE email= '" + email + "' AND password = '" + password + "'"
        cursor.execute(query)
        account = cursor.fetchone()

        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account[0]
            session['name'] = account[1]
            session['surname'] = account[2]
            session['email'] = account[4]

            # Redirect to home page
            return redirect(url_for('home.home', surname=account[2]))
        else:
            # Account doesnt exist or email/password incorrect
            msg = 'Incorrect email/password!'
    return render_template('login.html', msg=msg)


@bp.route('/logout')
def logout():
    # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('name', None)
    session.pop('surname', None)
    session.pop('email', None)
    # Redirect to login page
    return redirect(url_for('auth.login'))


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
