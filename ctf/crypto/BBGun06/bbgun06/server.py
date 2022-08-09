from encryption import RSA, bytes_to_long
from secret import FLAG
import socketserver
import signal


class Handler(socketserver.BaseRequestHandler):

    def handle(self):
        signal.alarm(0)
        main(self.request)


class ReusableTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass


def sendMessage(s, msg):
    s.send(msg.encode())


def recieveMessage(s, msg):
    sendMessage(s, msg)
    return s.recv(4096).decode().strip()


def parseEmail():
    with open("email.txt", "r") as f:
        data = f.readlines()
    user = data[0].strip()[len("From: "):]
    return user.encode(), "".join(data)


def generateHeaders(rsa, signature):
    signature = f"signature: {signature.hex()}\n"
    certificate = f"certificate: \n{rsa.export_key()}\n"
    return signature + certificate


def different(rsa, signature, forged_signature):
    signature = bytes_to_long(signature)
    forged_signature = bytes_to_long(forged_signature)
    if ((forged_signature % rsa.n) != signature):
        return True
    return False


def main(s):
    rsa = RSA(2048)

    user, data = parseEmail()

    signature = rsa.sign(user)
    rsa.verify(user, signature)

    headers = generateHeaders(rsa, signature)

    valid_email = headers + data
    sendMessage(s, valid_email + "\n\n")

    try:
        forged_signature = recieveMessage(s, "Enter the signature as hex: ")
        forged_signature = bytes.fromhex(forged_signature)

        if not rsa.verify(user, forged_signature):
            sendMessage(s, "Invalid signature")

        if different(rsa, signature, forged_signature):
            sendMessage(s, FLAG)
    except:
        sendMessage(s, "An error occured")


if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    server = ReusableTCPServer(("0.0.0.0", 1337), Handler)
    server.serve_forever()
