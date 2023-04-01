import functools

from flask import request, make_response, redirect, url_for

from cryptoutil import lj12_hash
from Crypto.Random import get_random_bytes
from urllib.parse import parse_qs

SECRET = get_random_bytes(50)


def view_as_guest(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        if 'login_info' not in request.cookies:
            resp = make_response(redirect(request.path))
            resp.set_cookie('login_info', create_cookie('guest'))
            return resp

        return func(*args, **kwargs)

    return wrapped


def verify_login(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        if not verify_cookie(request.cookies.get('login_info', '')):
            return redirect(url_for('web.login', error='You are not a logged in member'))

        return func(*args, **kwargs)
    return wrapped


def create_cookie(username, is_logged_in=False):
    data = f'user_id={username}&isLoggedIn={is_logged_in}'
    signature = lj12_hash(SECRET + data.encode())
    return data + '.' + signature


def verify_cookie(cookie_data):
    data, signature = cookie_data.split(".")

    if lj12_hash(SECRET + data.encode()) == signature:
        return {
            k: v[-1] for k, v in parse_qs(data).items()
        }.get('isLoggedIn', '') == 'True'

    return False
