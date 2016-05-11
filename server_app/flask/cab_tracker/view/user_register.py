from flask import Blueprint, request
from business_logic.user_profile_bl import data_is_valid, save_data_to_db
from common.constants import BLUEPRINTS

__author__ = 'cabtracker'


app_route = Blueprint(__name__, __name__)

@app_route.route(BLUEPRINTS['user_register'], methods=['POST'])
def create_new_user():
    if data_is_valid(request.data):
        save_data_to_db(request.data)
    return "new user created successfully..!!"