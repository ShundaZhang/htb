from Crypto.Util.Padding import pad, unpad
import json, os, db, time, jwt, datetime
from Crypto.Cipher import AES
from secret import FLAG

def recv(s):
    return input(s)

def send(s):
    print(s)

JWT_SECRET = os.urandom(32)
KEY = os.urandom(16)
IV  = os.urandom(16)

menu = """ \
|--------------------------------------------------------|
| Welcome to our information server                      |
| from here you can do the following                     |
| actions.                                               |
|--------------------------------------------------------|
| [1] Login                                              |
| [2] Retrieve user data                                 |
| [3] Draw money                                         |
| [4] Exit                                               |
|--------------------------------------------------------|

"""


def main():
    AUTH = False
    
    while True:
        send(menu)
        try:
            option = recv("> ")
            if option == "1":
                creds = recv("Send your credentials: ")
                creds = json.loads(creds)
                if creds["token"]:
                    cipher = AES.new(KEY, AES.MODE_CBC, IV)
                    try:
                        token = unpad(cipher.decrypt(bytes.fromhex(creds["token"])), 16)
                    except:
                        send("Decryption error!")
                    
                    try:
                        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
                        username = payload.get("username")
                        user_info = db.get_user_info(username)
                        AUTH = True
                    except:
                        send("Validation error!")

                else:
                    user_info = db.get_user_info(creds["username"])
                    if user_info == None or creds["password"] != user_info["password"]:
                        send("Incorrect username or password.")
                    else:
                        payload = {
                            "username": user_info["username"],
                            "exp": datetime.datetime.utcnow() + datetime.timedelta(days = 1)
                        }
                        token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
                        cipher = AES.new(KEY, AES.MODE_CBC, IV)
                        encrypted_token = cipher.encrypt(pad(token.encode(), 16))
                        send(f"Token: {encrypted_token.hex()}")
                        AUTH = True

            elif option == "2":
                if AUTH:
                    card_number = user_info["card_number"]
                    balance = str(user_info["balance"])
                    payload = card_number + balance
                    cipher = AES.new(KEY, AES.MODE_CBC, IV)
                    encrypted_data = cipher.encrypt(pad(payload.encode(), 16))
                    send(f"Encrypted data: {encrypted_data.hex()}")

            elif option == "3":
                if AUTH:
                    card_number = recv("Insert your card number: ")
                    if card_number == user_info["card_number"]:
                        draw = recv("Quantity: ")
                        result = db.withdraw_money(int(draw), user_info["username"])
                        if result:
                            if result[1] == 0:
                                send(f"Hey! You have managed to drop the target account to zero! Here's your flag: {FLAG}")

            elif option == "4":
                send("Goodbye!")
                break
            
            else:
                send("Invalid option!")

        except Exception as e:
            send(f"Oops! Something went wrong : {e}")

if __name__ == "__main__":
    db.create_db()
    main()