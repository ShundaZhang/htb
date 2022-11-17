from secret import FLAG
from hashlib import sha512
import socketserver
import signal
from random import randint

WELCOME = """
**************** Welcome to the Hash Game. ****************
*                                                         *
*    Hash functions are really spooky.                    *
*    In this game you will have to face your fears.       *
*    Can you find a colision in the updated sha512?       *
*                                                         *
***********************************************************
"""


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


class ahs512():

    def __init__(self, message):
        self.message = message
        self.key = self.generateKey()

    def generateKey(self):
        while True:
            key = randint(2, len(self.message) - 1)
            if len(self.message) % key == 0:
                break

        return key

    def transpose(self, message):
        transposed = [0 for _ in message]

        columns = len(message) // self.key

        for i, char in enumerate(message):
            row = i // columns
            col = i % columns
            transposed[col * self.key + row] = char

        return bytes(transposed)

    def rotate(self, message):
        return [((b >> 4) | (b << 3)) & 0xff for b in message]

    def hexdigest(self):
        transposed = self.transpose(self.message)
        rotated = self.rotate(transposed)
        return sha512(bytes(rotated)).hexdigest()


def main(s):
    sendMessage(s, WELCOME)

    original_message = b"pumpkin_spice_latte!"
    original_digest = ahs512(original_message).hexdigest()
    sendMessage(
        s,
        f"\nFind a message that generate the same hash as this one: {original_digest}\n"
    )

    while True:
        try:
            message = receiveMessage(s, "\nEnter your message: ")
            message = bytes.fromhex(message)

            digest = ahs512(message).hexdigest()

            if ((original_digest == digest) and (message != original_message)):
                sendMessage(s, f"\n{FLAG}\n")
            else:
                sendMessage(s, "\nConditions not satisfied!\n")

        except KeyboardInterrupt:
            sendMessage(s, "\n\nExiting")
            exit(1)

        except Exception as e:
            sendMessage(s, f"\nAn error occurred while processing data: {e}\n")


if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    server = ReusableTCPServer(("0.0.0.0", 1337), Handler)
    server.serve_forever()
