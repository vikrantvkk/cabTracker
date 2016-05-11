__author__ = 'cabtracker'


BASE_URL = ''
USER_PATH = '/user'
HOST = '0.0.0.0'
PORT = 7887

BLUEPRINTS = {'login': BASE_URL + '/login',
              'logout': BASE_URL +'/logout',
              'user_profile': BASE_URL + USER_PATH + '/profile',
              'user_register': BASE_URL + USER_PATH + '/register'

}

STATUS_SUCCESS = 200
STATUS_USER_INVALID = 400
STATUS_INVALID_ACCESS = 404