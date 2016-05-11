from flask import request, session, make_response

from common.constants import STATUS_INVALID_ACCESS

__author__ = 'cabtracker'


def get_user_info():
    return {}


def login_required(method):
    if request.form['username'] in session:
        return method
    else:
        return make_response('Login required', STATUS_INVALID_ACCESS)