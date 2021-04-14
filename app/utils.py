import os
from flask import current_app, send_file


def get_id_card_file(filename):
    return send_file(os.path.join(os.getcwd() + '/' + current_app.config['UPLOAD_FOLDER'], filename))
