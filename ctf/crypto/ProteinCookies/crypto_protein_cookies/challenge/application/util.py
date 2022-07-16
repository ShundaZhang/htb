from flask import request, make_response, redirect, url_for
from .models import session
import functools

def view_as_guest(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        if 'login_info' not in request.cookies:
            resp = make_response(redirect(request.path))
            
            resp.set_cookie('login_info', session.create('guest'))
            return resp

        return func(*args, **kwargs)
    return wrapped

def verify_login(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        if not session.validate_login(request.cookies.get('login_info', '')):
            return redirect(url_for('web.login', error='You are not a logged in member'))

        return func(*args, **kwargs)
    return wrapped