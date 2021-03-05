from flask import Blueprint, session, current_app, send_file, render_template, request
from database import db
from app.utils import get_id_card_file

bp = Blueprint('idcard', __name__, url_prefix='/idcard')


@bp.route('/showidcard')
def showidcard():
    session_id = str(session['id'])
    cursor = db.connection.cursor()
    cursor.execute("SELECT filename FROM accounts WHERE ID = " + session_id)
    filename = cursor.fetchone()[0]

    return render_template('idcard.html', filename=filename)


@bp.route('/document')
def getidcard():
    filename = request.args.get('filename')
    doc_file = get_id_card_file(filename)
    return doc_file

