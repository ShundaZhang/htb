from flask import render_template, Blueprint, send_file
from ..util import view_as_guest, verify_login

web = Blueprint('web', __name__)
api = Blueprint('api', __name__)

@web.before_request
@view_as_guest
def before_request():
    pass

@web.route('/')
def index(): 
    return render_template('index.html')

@web.route('/login')
def login(): 
    return render_template('login.html')

@api.route('/login', methods=['POST'])
def login_api():
    return {'error' : 1, 'message': 'Wrong email or password.'}, 400


@web.route('/register')
def register(): 
    return render_template('register.html')

@api.route('/register', methods=['POST'])
def register_api():
    return {'error': 1, 'message': 'Registrations are temporarily closed due to high load'}, 400

@web.route('/program')
@verify_login
def program():
    return send_file('flag.pdf')