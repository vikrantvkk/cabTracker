from flask import Blueprint, session, request, make_response, jsonify

from business_logic.login_bl import is_user_validate
from common.constants import BLUEPRINTS, STATUS_USER_INVALID, STATUS_SUCCESS
from common.helper import get_user_info

__author__ = 'cabtracker'


app_route = Blueprint(__name__, __name__)

@app_route.route(BLUEPRINTS['login'], methods=['POST'])
def login():
    if is_user_validate():
        session['username'] = request.form['username']
        return make_response(jsonify({'data': get_user_info()}), STATUS_SUCCESS)
    else:
        return make_response('User Not Valid', STATUS_USER_INVALID)