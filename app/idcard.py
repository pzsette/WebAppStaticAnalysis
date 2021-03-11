from flask import Blueprint, session, current_app, render_template, request, send_from_directory
from app.models.user import User
import os

bp = Blueprint('idcard', __name__, url_prefix='/idcard')


@bp.route('/showidcard')
def showidcard():
    session_id = str(session['id'])
    filename = User.query.filter_by(id=session_id).first().filename
    return render_template('idcard.html', filename=filename)


@bp.route('/document')
def getidcard():
    filename = request.args.get('filename')
    directory = os.path.abspath(current_app.config['UPLOAD_FOLDER'])
    return send_from_directory(directory=directory, filename=filename)
