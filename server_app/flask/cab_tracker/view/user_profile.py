from flask import Blueprint
from common.constants import BLUEPRINTS

__author__ = 'cabtracker'


app_route = Blueprint(__name__, __name__)

@app_route.route(BLUEPRINTS['user_profile'])
def user_profile():
    return "User Name: Vikrant"
