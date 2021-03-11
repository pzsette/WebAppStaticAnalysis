from flask import session, render_template, redirect, url_for, Blueprint, request
from markupsafe import Markup
from app.models.user import User
from app.models.action import Action
import hashlib

bp = Blueprint('home', __name__, url_prefix='/home')


@bp.route('/')
def home(msg=None):
    if 'loggedin' in session:
        session_id = session['id']
        operations = Action.query.filter_by(id_user=session_id).all()
        user = User.query.filter_by(id=session_id).first()

        return render_template('home.html', balance=user.amount, msg=msg, operationsList=operations)
    return redirect(url_for('auth.login'))


@bp.route('/action', methods=['POST'])
def actions():
    if request.method == 'POST':
        causal = request.form["causal"]
        session_id = str(session['id'])

        current_user = User.query.filter_by(id=session_id).first()
        psw = current_user.password

        if psw == hashlib.sha256(request.form["password"].encode("utf8")).hexdigest():
            actual_balance = current_user.amount
            amount = int(Markup.escape(request.form["amount"]))
            if request.form["action"] == 'Withdraw':
                if (actual_balance - amount) >= 0:
                    new_balance = actual_balance - amount
                    current_user.amount = new_balance
                    new_action = Action(session_id, amount, causal, 'withdraw')
                    Action.add(new_action)
                else:
                    return home(msg="You don't have enough money")
            else:
                new_balance = actual_balance + amount
                User.query.filter_by(id=session_id).first().amount = new_balance
                new_action = Action(session_id, amount, causal, 'deposit')
                Action.add(new_action)
        return home(msg="Wrong password!")
