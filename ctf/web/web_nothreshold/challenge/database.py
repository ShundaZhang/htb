from app.config import Config
from flask import g
import sqlite3


def query_db(query, args=(), one=False):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute(query, args)
    rv = [
        dict((cursor.description[idx][0], value) for idx, value in enumerate(row))
        for row in cursor.fetchall()
    ]
    return (rv[0] if rv else None) if one else rv


def connect_db():
    return sqlite3.connect(Config.DATABASE_URI, isolation_level=None)


def close_db():
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()
