import os, json, random

from urllib.parse import urlparse

generate = lambda x: os.urandom(x).hex()

def json_response(message, message_type, error=False):
    key = "error" if error else "success"
    return json.dumps({
        key: {
            "type": message_type,
            "message": message
        }
    })

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def is_request_from_localhost(handler):
    if handler.request.remote_ip in ["127.0.0.1", "::1"]:
        return True
    return False

def update_tornados(tornado, updated):
    for index, value in tornado.items():
        if hasattr(updated, "__getitem__"):
            if updated.get(index) and type(value) == dict:
                update_tornados(value, updated.get(index))
            else:
                updated[index] = value
        elif hasattr(updated, index) and type(value) == dict:
            update_tornados(value, getattr(updated, index))
        else:
            setattr(updated, index, value)

def read_file_contents(file_path):
    try:
        with open(file_path, "r") as file:
            contents = file.read()
        return contents
    except FileNotFoundError:
        return f"Error: The file at {file_path} was not found."
    except IOError as e:
        return f"Error: An I/O error occurred. {str(e)}"

def random_ip():
    return f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"

def random_hostname():
    return f"host-{random.randint(1000, 9999)}"

def random_status():
    return random.choice(["active", "inactive"])