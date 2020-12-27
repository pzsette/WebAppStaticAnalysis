from flask import session, render_template_string, render_template, redirect, url_for, Blueprint, request, flash
from database import db

bp = Blueprint('home', __name__, url_prefix='/home')


@bp.route('/')
def home(msg=None):
    if 'loggedin' in session:

        session_id = str(request.args.get('sessionId'))

        cursor = db.connection.cursor()

        cursor.execute("SELECT * FROM operations WHERE idUser ="+session_id)
        operations_list = cursor.fetchall()

        # HARDCODED SQL
        query = "SELECT amount FROM accounts WHERE id = "+session_id
        cursor.execute(query)

        # SECURE VERSION
        # cursor.execute(" SELECT amount FROM accounts WHERE id = %s", session_id))

        data = cursor.fetchone()[0]
        if msg is None:
            '''home = open('templates/home.html').read()
            param = '<script>alert(1)</script>'
            resp = home.replace('{{ name }}', param)
            return render_template_string(resp, balance=data, operationsList=operations_list)'''

            return render_template('home.html', balance=data, operationsList=operations_list)
        else:
            return render_template('home.html', balance=data, msg=msg, operationsList=operations_list)
    return redirect(url_for('auth.login'))


@bp.route('/action', methods=['POST', 'GET'])
def actions():
    if request.method == 'POST':
        causal = request.form["causal"]
        cursor = db.connection.cursor()
        session_id = str(session['id'])
        cursor.execute("SELECT password FROM accounts WHERE id ="+session_id)
        psw = cursor.fetchone()
        if psw:
            if psw[0] == request.form["password"]:
                cursor.execute("SELECT amount FROM accounts WHERE id = "+session_id)
                actual_amount = cursor.fetchone()
                if request.form["action"] == 'Withdraw':
                    if (int(actual_amount[0]) - int(request.form["amount"])) >= 0:
                        new_balance = int(actual_amount[0]) - int(request.form["amount"])
                        cursor.execute("UPDATE accounts SET amount = %s WHERE id = %s", (new_balance, session_id))
                        cursor.execute("INSERT INTO operations (idUser, amount, causal ,operationType) VALUES "
                                       "(%s, %s, %s, %s)", (session_id, request.form["amount"], causal, 'withdraw'))
                        db.connection.commit()
                    else:
                        msg="You don't have enough money!"
                        return home(msg=msg)
                else:
                    new_balance = int(actual_amount[0]) + int(request.form["amount"])
                    cursor.execute("UPDATE accounts SET amount = %s WHERE id = %s", (new_balance, session_id))
                    cursor.execute("INSERT INTO operations (idUser, amount, causal ,operationType) VALUES "
                                   "(%s, %s, %s, %s)", (session_id, request.form["amount"], causal, 'deposit'))
                    db.connection.commit()
    return home()


@bp.route('/operations')
def operations():
    cursor = db.connect.cursor()
    cursor.execute("SELECT * FROM operations")
    result = cursor.fetchone()
    date = result[2].date()
    return 'op'
