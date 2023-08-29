from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

#from secret import FLAG
FLAG = "HTB{F4K3_f149_4_73571N9!!!}"

class AAES():
    def __init__(self):
        self.padding = "CryptoHackTheBox"

    def pad(self, plaintext):
        return plaintext + self.padding[:(-len(plaintext) % 16)] + self.padding

    def encrypt(self, plaintext):
        cipher = AES.new(os.urandom(16), AES.MODE_ECB)
        return cipher.encrypt(pad(plaintext, 16))


def main():
    aaes = AAES()

    while True:
        message = input("Message for encryption: ")
        plaintext = aaes.pad(message) + aaes.pad(FLAG)
        print(plaintext)
        print(aaes.encrypt(plaintext.encode()).hex())


if __name__ == "__main__":
    main()
