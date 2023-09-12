import json
import os
from Crypto.PublicKey import RSA
import base64
from hashlib import sha512
from binascii import unhexlify

class Wallet(object):

    def __init__(self, key_file=None):
        if key_file is None:
            print("[+] WARNING: KEYS NOT SAVED TO DISK")
            self.wallet = RSA.generate(1024)
            self.address = base64.b64encode(self.wallet.public_key().export_key("PEM")).decode()
        else:
            if not os.path.exists(key_file):
                self.wallet = RSA.generate(1024)
                with open(key_file, "wb") as f:
                    f.write(self.wallet.export_key("PEM"))
            else:
                self.wallet = RSA.import_key(open(key_file).read())

            self.address = base64.b64encode(self.wallet.public_key().export_key("PEM")).decode()

    def save(self, key_file):
        with open(key_file, "wb") as f:
            f.write(self.wallet.export_key("PEM"))

    def sign_message(self, message) -> int:
        if type(message) == dict:
            message = json.dumps(message)
        if type(message) != bytes:
            message = message.encode()

        h = int.from_bytes(sha512(message).digest(), byteorder="big")
        sig = pow(h, self.wallet.d, self.wallet.n)
        return sig

    @staticmethod
    def verify_message(key, message, sig) -> bool:
        if type(message) == dict:
            message = json.dumps(message)
        if type(message) != bytes:
            message = message.encode()

        if type(sig) == str:
            if len(sig) % 2 == 1:
                sig = "0" + sig
            sig = int.from_bytes(unhexlify(sig), byteorder="big")
        

        h = int.from_bytes(sha512(message).digest(), byteorder="big")
        hashFromSignature = pow(sig, key.e, key.n)
        return h == hashFromSignature