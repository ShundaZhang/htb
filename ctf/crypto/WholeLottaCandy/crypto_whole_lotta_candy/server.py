from encrypt import Encryptor
from secret import FLAG
import socketserver
import random
import signal
import json

MODES = ['ECB', 'CBC', 'CFB', 'OFB', 'CTR']


class Handler(socketserver.BaseRequestHandler):

    def handle(self):
        signal.alarm(0)
        main(self.request)


class ReusableTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass


def sendMessage(s, msg):
    s.send(msg.encode())


def receiveMessage(s, msg):
    sendMessage(s, msg)
    return s.recv(4096).decode().strip()


def main(s):
    mode = random.choice(MODES)
    enc = Encryptor()
    while True:
        try:
            sendMessage(s,
                        f"Please interact with the server using json data!\n")
            sendMessage(s, f"Selected mode is {mode}.\n")
            payload = receiveMessage(
                s,
                "\nOptions:\n\n1.Encrypt flag\n2.Encrypt plaintext\n3.Change mode\n4.Exit\n\n> "
            )
            payload = json.loads(payload)
            option = payload["option"]
            if option == "1":
                ciphertext = enc.encrypt(FLAG, mode).hex()
                response = json.dumps({
                    "response": "encrypted",
                    "ciphertext": ciphertext
                })
                sendMessage(s, "\n" + response + "\n")
            elif option == "2":
                payload = receiveMessage(s, "Enter plaintext: \n")
                payload = json.loads(payload)
                plaintext = payload['plaintext'].encode()
                ciphertext = enc.encrypt(plaintext, mode).hex()
                response = json.dumps({
                    "response": "encrypted",
                    "ciphertext": ciphertext
                })
                sendMessage(s, "\n" + response + "\n")
            elif option == "3":
                response = json.dumps({"modes": MODES})
                sendMessage(
                    s, "These are the supported modes\n" + response + "\n")
                payload = receiveMessage(s, "Expecting modes: \n")
                payload = json.loads(payload)
                mode = random.choice(payload['modes'])
            elif option == "4":
                sendMessage(s, "Bye bye\n")
                exit()
        except Exception as e:
            response = json.dumps({"response": "error", "message": str(e)})
            sendMessage(s, "\n" + response + "\n")
            exit()


if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    server = ReusableTCPServer(("0.0.0.0", 1337), Handler)
    server.serve_forever()
