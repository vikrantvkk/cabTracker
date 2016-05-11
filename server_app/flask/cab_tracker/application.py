from flask import Flask
from app_bootstrap import register_blueprints
from common.constants import BLUEPRINTS, HOST, PORT

__author__ = 'cabtracker'


app = Flask(__name__)
app.secret_key = "\xd7;\xf3y\x87\x8c*\xd0\xe9\xa3\xce\xad%c\x88\xebYO\xe4\x08l'\x17\x96"
register_blueprints(app, BLUEPRINTS)

if __name__ == '__main__':
    app.run(HOST, PORT, debug=True)
