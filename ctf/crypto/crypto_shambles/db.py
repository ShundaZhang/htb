from secret import db_info
import sqlite3

def create_db():
    try:
        connection = sqlite3.connect("users.db")
        connection.execute("""CREATE TABLE users (
                code integer primary key AUTOINCREMENT,
                username text,
                password text,
                balance float,
                card_number text
        )""")

        for user in db_info:
            connection.execute("insert into users(username, password, balance, card_number) values (?, ?, ?, ?)", user)

        connection.commit()
        connection.close()
    except Exception as e:
        print(e)

def get_user_info(username):
    connection = sqlite3.connect("users.db")
    cursor = connection.execute("select username, password, balance, card_number from users where username = ?", (username, ))
    user_info = cursor.fetchone()
    if user_info != None:
        return {"username": user_info[0], "password": user_info[1], "balance": user_info[2], "card_number": user_info[3]}
    else:
        return None


def withdraw_money(amount, user):
    connection = sqlite3.connect("users.db")
    cursor = connection.execute("SELECT username, balance FROM users WHERE username = ?", (user, ))
    user_info = cursor.fetchone()
    if user_info is not None:
        money_left = float(user_info[1]) - float(amount)
        assert money_left >= 0
        connection.execute("UPDATE users SET balance = ? WHERE username = ?", (money_left, user))
        connection.commit()
        connection.close()
        return True, money_left
    else:
        return False, -1
    