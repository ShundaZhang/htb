from application.database import *
from flask import Blueprint, session, jsonify, redirect, render_template, request, make_response, current_app
from application.util import response, isAuthenticated
import datetime, sys, requests

web = Blueprint('web', __name__)
api = Blueprint('api', __name__)

@web.route('/')
def login():
    return render_template('login.html')

@web.route('/home')
@isAuthenticated
def home(decoded_token):
    user = getUser(decoded_token.get('username'))
    flag = getFlag()
    
    if(flag[0].get('show_flag') == 1):
        return render_template('home.html', user=user[0], flag=flag[0].get('flag'))


    return render_template('home.html', user=user[0])

@web.route('/logout')
def logout():
    res = make_response(redirect('/'))
    res.set_cookie('session', '', expires=0)
    return res

@api.route('/login', methods=['POST'])
def api_login():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
        
    if not username or not password:
        return response('All fields are required!'), 401
    
    user = login_user_db(username, password)
    
    if user:
        res = response('Logged in successfully!')
        res.status_code = 200
        res.set_cookie('session', user, expires=datetime.datetime.utcnow() + datetime.timedelta(minutes=360), httponly=False)
        return res

    return response('Invalid credentials!'), 403

@api.route('/register', methods=['POST'])
def api_register():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    
    if not username or not password:
        return response('All fields are required!'), 401
    
    user = register_user_db(username, password)
    
    if user:
        return response('User registered! Please login'), 200
        
    return response('User already exists!'), 403

@api.route('/withdraw', methods=['POST'])
@isAuthenticated
def withdraw(decoded_token):
    body = request.get_data()
    amount = request.form.get('amount', '')
    account = request.form.get('account', '')
    
    if not amount or not account:
        return response('All fields are required!'), 401
    
    user = getUser(decoded_token.get('username'))

    try:
        if (int(user[0].get('balance')) < int(amount) or int(amount) < 0 ):
            return response('Not enough credits!'), 400

        res = requests.post(f"http://{current_app.config.get('PHP_HOST')}/api/withdraw", 
            headers={"content-type": request.headers.get("content-type")}, data=body)
        
        jsonRes = res.json()

        return response(jsonRes['message'])
    except:
        return response('Only accept number!'), 500