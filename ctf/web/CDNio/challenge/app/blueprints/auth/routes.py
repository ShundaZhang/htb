from . import auth_bp

from flask import request, jsonify, current_app, render_template

import datetime, uuid, sqlite3, jwt


def get_db_connection():
    conn = sqlite3.connect("/www/app/database.db")
    conn.row_factory = sqlite3.Row
    return conn

def generate_api_key():
    return str(uuid.uuid4()) 

@auth_bp.route('/', methods=['POST', 'GET'])
def search():

    if request.method == 'POST':
        data = request.get_json()

        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return jsonify({"message": "username or password are required!"}), 400

        conn = get_db_connection()

        user = conn.execute(
            "SELECT * FROM users WHERE username = ?", (username,)
        ).fetchone()
        conn.close()

        if user and user["password"] == password:

            token = jwt.encode(
                {
                    "sub": user["username"],
                    "iat": datetime.datetime.utcnow(),
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),
                },
                current_app.config["JWT_SECRET_KEY"],
                algorithm="HS256",
            )

            return jsonify({"token": f"{token}"}), 200

        else:
            return jsonify({"message": "Credentials not found. Please check your username and password."}), 404

    else:
        return render_template('search.html')



@auth_bp.route('/register', methods=['POST', 'GET'])
def register():

    if request.method == 'POST':
        data = request.get_json()

        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        if not username or not password or not email:
            return jsonify({"message": "username, password, and email are required!"}), 400

        conn = get_db_connection()

        existing_user = conn.execute(
            "SELECT * FROM users WHERE username = ? OR email = ?", (username, email,)
        ).fetchone()

        if existing_user:
            conn.close()
            return jsonify({"message": "Username or email already exists!"}), 409

        api_key = generate_api_key()

        conn.execute(
            """
            INSERT INTO users (username, password, email, api_key, created_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (username, password, email, api_key, datetime.datetime.utcnow())
        )

        conn.commit()
        conn.close()

        return jsonify({"message": f"User {username} registered successfully!"}), 201

    else:
        return render_template('register.html')