from . import main_bp

from app.middleware.auth import jwt_required
from flask import jsonify, request

import re, sqlite3

def get_db_connection():
    conn = sqlite3.connect("/www/app/database.db")
    conn.row_factory = sqlite3.Row
    return conn

@main_bp.route('/<path:subpath>', methods=['GET'])
@jwt_required
def profile(subpath):
    
    if re.match(r'.*^profile', subpath): # Django perfection

        decoded_token = request.decoded_token

        username = decoded_token.get('sub')
        if not username:
            return jsonify({"error": "Invalid token payload!"}), 401

        conn = get_db_connection()

        user = conn.execute(
            "SELECT id, username, email, api_key, created_at, password FROM users WHERE username = ?",
            (username,)
        ).fetchone()
        conn.close()
        
        if user:
            return jsonify({
                "id": user["id"],
                "username": user["username"],
                "email": user["email"],
                "password": user["password"],
                "api_key": user["api_key"],
                "created_at": user["created_at"]
            }), 200

        else:
            return jsonify({"error": "User not found"}), 404
        
    else:
        return jsonify({"error": "No match"}), 404