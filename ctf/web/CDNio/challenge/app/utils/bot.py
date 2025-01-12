import time, os, threading, requests

base_url = "http://0.0.0.0:1337"

admin_passwd = os.getenv("RANDOM_PASSWORD")

base_headers = {
    "User-Agent": "CDNio Bot ()"
}

def login_and_get_token():
    session = requests.Session()

    login_url = f"{base_url}/"
    payload = {
        "username": "admin",
        "password": admin_passwd
    }
    response = session.post(login_url, json=payload, headers=base_headers)

    if response.status_code == 200:
        token = response.json().get("token")
        return token, session 
    else:
        return None, None  

def bot_runner(uri):

    token, session = login_and_get_token()
    
    headers  = {
        **base_headers,
        "Authorization": f"Bearer {token}"
    }

    r = requests.get(f"{base_url}/{uri}", headers=headers)

    time.sleep(5) 

def bot_thread(uri):
    bot_runner(uri)
