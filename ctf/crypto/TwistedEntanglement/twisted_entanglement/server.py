from util import *
import socketserver
import signal
from secret import FLAG, private_key

menu = ('\n\n|---------------------------------------|\n' +
        '| Welcome to Twisted Entanglement!      |\n' +
        '| Maybe we can change the Crypto world  |\n' +
        '| with a physical phenomena :D          |\n' +
        '|---------------------------------------|\n' +
        '| [1] Test our SuperMegaHyperSecure     |\n' +
        '|     Elliptic Curve ;)                 |\n' +
        '| [2] Play with our Qubits ^__^         |\n' +
        '| [3] Abort Mission X__X                |\n' +
        '|---------------------------------------|\n')

assert private_key < 8748541127929402731638

p = 115792089237316195423570985008687907853269984665640564039457584007908834671663
a = 0
b = 7
E = {"a": a, "b": b, "p": p}


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
    G = [
        0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
        0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
    ]
    Q = multiply(private_key, G, E)
    sendMessage(s, f"Public Key: {Q}")

    while True:
        sendMessage(s, menu)
        try:
            option = receiveMessage(s, "\n> ")
            if option == "1":
                user_point = receiveMessage(s, "\nEnter your point x,y: ")
                point = parseUserPoint(user_point)
                public_key = multiply(private_key, point, E)
                sendMessage(s, f"\nHere's your new Public Key: {public_key}")
            elif option == "2":
                user_basis = receiveMessage(
                    s, "\nChoose your 256 basis for the KEP: ")

                basis = parseUserBasis(user_basis)
                q_server_key, q_user_key = generateKeys(basis, private_key)
                ciphertext = encrypt(FLAG, q_server_key)

                sendMessage(s, f"\nThe Quantum key: {q_user_key}")
                sendMessage(s, f"\nFlag Encrypted: {ciphertext.hex()}")

            elif option == "3":
                sendMessage(s, "\nQuantum Goodbye!")
                break
            else:
                sendMessage(s, "\nInvalid option!")
        except Exception as e:
            sendMessage(s, f"\nOoops! something strange happen X__X: {e}")


if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    server = ReusableTCPServer(("0.0.0.0", 1337), Handler)
    server.serve_forever()
