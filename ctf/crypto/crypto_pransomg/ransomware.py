from Crypto.Util.number import long_to_bytes as l2b
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
from random import getrandbits
import os, sys


class Encryptor:

    def __init__(self):
        self.out_dir = 'enc_files'
        self.counter = 0
        self.otp = os.urandom(2)
        self.initialize()

    def initialize(self):
        os.makedirs(f'./{self.out_dir}', exist_ok=True)

        self.secrets = []

        for _ in range(32):
            self.secrets.append(getrandbits(576))

        self.key = l2b(getrandbits(1680))[:16]
        self.iv = l2b(getrandbits(1680))[:16]

        self.cipher = AES.new(self.key, AES.MODE_CBC, self.iv)

    def _xor(self, a, b):
        return b''.join([bytes([a[i] ^ b[i % len(b)]]) for i in range(len(a))])

    def encrypt(self, target):
        for fname in os.listdir(target):
            with open(f'{target}/{fname}') as f:
                contents = f.read().rstrip().encode()

            enc_fname = f"{str(self.counter + 1)}_{fname.split('.')[0]}.enc"

            enc = self.cipher.encrypt(pad(contents, 16))
            enc += self._xor(l2b(self.secrets[self.counter]), self.otp)

            self.write(enc_fname, enc)
            self.counter += 1

    def write(self, filepath, data):
        with open(f'{self.out_dir}/{filepath}', 'wb') as f:
            f.write(data)

def main():
    encryptor = Encryptor()
    encryptor.encrypt(sys.argv[1])

if __name__ == "__main__":
    main()
