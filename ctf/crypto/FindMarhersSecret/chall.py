import random
import signal
import subprocess
import socketserver
import json
import os
from Crypto.Cipher import ARC4, AES
import os
import hashlib
from secret import FLAG, KEY


def encrypt(key, iv, pt):
    return ARC4.new(iv + key).encrypt(pt).hex()


def challenge(req):
    key = bytes.fromhex(KEY)
    assert(len(key) == 27)
    req.sendall(b'Connected to the cyborg\'s debugging interface\n')
    while True:
        req.sendall(
            b'\nOptions:\n1. Encrypt your text.\n2. Claim the key.\n> ')
        try:
            response = json.loads(req.recv(4096).decode())
            if response['option'] == 'encrypt':
                iv = bytes.fromhex(response['iv'])
                pt = bytes.fromhex(response['pt'])
                ct = encrypt(key, iv, pt)
                payload = {'response': 'success',
                           'pt': response['pt'], 'ct': ct}
                payload = json.dumps(payload)
                req.sendall(payload.encode())
            elif response['option'] == 'claim':
                answer = bytes.fromhex(response['key'])
                if hashlib.sha256(answer).hexdigest() == hashlib.sha256(key).hexdigest():
                    payload = {'response': 'success', 'flag': FLAG}
                    payload = json.dumps(payload)
                    req.sendall(payload.encode())
                else:
                    payload = {'response': 'fail',
                               'message': 'Better luck next time.'}
                    payload = json.dumps(payload)
                    req.sendall(payload.encode())

            else:
                payload = {'response': 'error', 'message': 'Invalid option!'}
                payload = json.dumps(payload)
                req.sendall(payload.encode())
        except Exception as e:
            payload = json.dumps(
                {'response': 'error', 'message': 'An error occured!'})
            req.sendall(payload.encode())
            return


class incoming(socketserver.BaseRequestHandler):
    def handle(self):
        signal.alarm(6000)
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
