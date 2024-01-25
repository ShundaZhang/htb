from application.util import createJWT
from flask_mysqldb import MySQL
import MySQLdb.cursors, secrets

mysql = MySQL()

def query(query, args=(), one=False):
    cursor = mysql.connection.cursor()
    cursor.execute(query, args)
    rv = [dict((cursor.description[idx][0], value)
        for idx, value in enumerate(row)) for row in cursor.fetchall()]
    return (rv[0] if rv else None) if one else rv


def login_user_db(username, password):
    user = query('SELECT username FROM users WHERE username = %s AND password = %s', (username, password,), one=True)
    
    if user:
        token = createJWT(user['username'])
        return token
    else:
        return False

def register_user_db(username, password):
    check_user = query('SELECT username FROM users WHERE username = %s', (username,), one=True)

    if not check_user:
        query('INSERT INTO users(username, password, wallet_address) VALUES(%s, %s, %s)', (username, password,secrets.token_hex(16), ))
        mysql.connection.commit()
        
        return True
    
    return False


def getUser(username):
    return query('SELECT * from users WHERE username = %s', (username, ))

def getFlag():
    return query('SELECT * from flag')
