from flask import request, jsonify, current_app
from functools import wraps
import jwt

def decode_jwt_token(token):
    try:
        payload = jwt.decode(token, current_app.config["JWT_SECRET_KEY"], algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return {"error": "Token has expired."}
    except jwt.InvalidTokenError:
        return None
    except Exception as e:
        print(f"Unexpected error decoding JWT: {str(e)}")  
        return None

def jwt_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization', '').strip()
        
        if not auth_header.startswith('Bearer '):
            return jsonify({"error": "Token is missing or invalid!"}), 401

        token = auth_header.split(" ", 1)[1].strip()
        decoded_token = decode_jwt_token(token)

        if decoded_token is None:
            return jsonify({"error": "Invalid token!"}), 401
        elif "error" in decoded_token:
            return jsonify(decoded_token), 401 

        request.decoded_token = decoded_token
        
        return f(*args, **kwargs)
    
    return decorated_function