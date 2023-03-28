from os import urandom
from Crypto.Cipher import AES
from secret import MESSAGE

assert all([x.isupper() for x in MESSAGE])
assert MESSAGE.startswith('A')


class Cipher:

    def __init__(self):
        self.salt = urandom(14)
        key = urandom(16)
        self.cipher = AES.new(key, AES.MODE_ECB)

    def encrypt(self, message):
        return [
            self.cipher.encrypt(message[i:i + 2].encode() + self.salt)
            for i in range(len(message) - 1)
        ]


def main():
    cipher = Cipher()

    encrypted = cipher.encrypt(MESSAGE)
    encrypted = "\n".join([c.hex() for c in encrypted])

    with open("output.txt", 'w+') as f:
        f.write(encrypted)


if __name__ == "__main__":
    main()
