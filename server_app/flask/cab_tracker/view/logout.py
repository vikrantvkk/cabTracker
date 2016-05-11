from flask import Blueprint, session, request, make_response
from common.constants import BLUEPRINTS, STATUS_SUCCESS, STATUS_USER_INVALID
from common.helper import login_required

__author__ = 'cabtracker'


app_route = Blueprint(__name__, __name__)

@app_route.route(BLUEPRINTS['logout'], methods=['POST'])
@login_required
def logout():
    user = session.pop(request.form['username'], None)
    if user is not None:
        return make_response("Logged out successfully", STATUS_SUCCESS)
    else:
        return make_response("Username not valid", STATUS_USER_INVALID)