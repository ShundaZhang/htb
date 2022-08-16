from hashlib import sha256
from Crypto.Util.Padding import pad, unpad
import signal
import subprocess
import socketserver
import os

allowed_commands = [b'whoami', b'ls', b'cat secret.txt', b'pwd']
BLOCK_SIZE = 32


def encrypt_block(block, secret):
    enc_block = b''
    for i in range(BLOCK_SIZE):
        val = (block[i]+secret[i]) % 256
        enc_block += bytes([val])
    return enc_block


def encrypt(msg, password):
    h = sha256(password).digest()
    if len(msg) % BLOCK_SIZE != 0:
        msg = pad(msg, BLOCK_SIZE)
    blocks = [msg[i:i+BLOCK_SIZE] for i in range(0, len(msg), BLOCK_SIZE)]
    ct = b''
    for block in blocks:
        enc_block = encrypt_block(block, h)
        h = sha256(enc_block + block).digest()
        ct += enc_block

    return ct.hex()


def run_command(cmd):
    if cmd in allowed_commands:
        try:
            resp = subprocess.run(
                cmd.decode().split(' '),  capture_output=True)
            output = resp.stdout
            return output
        except:
            return b'Something went wrong!\n'
    else:
        return b'Invalid command!\n'


def challenge(req):
    req.sendall(b'This is Jenny! I am the heart and soul of this spaceship.\n' +
                b'Welcome to the debug terminal. For security purposes I will encrypt any responses.')
    while True:
        req.sendall(b'\n> ')
        command = req.recv(4096).strip()
        output = run_command(command)
        response = b'Command executed: ' + command + b'\n' + output
        password = os.urandom(32)
        ct = encrypt(response, password)
        req.sendall(ct.encode())


class incoming(socketserver.BaseRequestHandler):
    def handle(self):
        signal.alarm(30)
        req = self.request
        challenge(req)


class ReusableTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass


def main():
    socketserver.TCPServer.allow_reuse_address = True
    server = ReusableTCPServer(("0.0.0.0", 1337), incoming)
    server.serve_forever()


if __name__ == "__main__":
    main()
