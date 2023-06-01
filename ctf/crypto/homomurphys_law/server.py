import socketserver
import signal
from encryption import *
import time


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


def readFile(name):
    with open(name, "rb") as f:
        data = f.read()
    return data


def AESEncrypt(aes, key):
    aes.setKey(key)
    data = readFile("note.txt")
    ts = time.time()
    for _ in range(1000):
        enc_file = aes.encrypt(data)
    te = time.time()
    return te - ts, enc_file


def main(s):
    gm = GM()
    obf = OBF()
    while True:
        aesp, aesc = AESP(), AESC()
        try:
            sendMessage(s, "Awaiting for encryption key\n\n")

            enc_key = [recieveMessage(s, "> ") for _ in range(128)]
            enc_key = [int(i) for i in enc_key]

            obf_key = gm.decrypt(enc_key)
            key = obf.deobfuscate(obf_key)

            choice = recieveMessage(
                s, "\nChoose what library you want to benchmark:\n\n"
                "[1] - PyCrypto AES Encrypt\n"
                "[2] - cryptography AES Encrypt\n\n> ")

            if choice == "1":
                time, enc_file = AESEncrypt(aesp, key)
            elif choice == "2":
                time, enc_file = AESEncrypt(aesc, key)
            else:
                sendMessage(s, "Invalid choice!\n")
                exit()

            sendMessage(s, enc_file.hex() + "\n")
            sendMessage(s, str(time) + "\n")

        except Exception as e:
            sendMessage(s, "Unexpected error.\n")
            print(e)


if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    server = ReusableTCPServer(("0.0.0.0", 1337), Handler)
    server.serve_forever()
