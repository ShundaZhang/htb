from Crypto.Util.number import isPrime, long_to_bytes, getPrime
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from random import randint
from hashlib import sha256

from secret import FLAG


class DH:

    def __init__(self):
        self.gen_params()

    def gen_params(self):
        self.r = getPrime(512)

        while True:
            self.q = getPrime(42)
            self.p = (2 * self.q * self.r) + 1
            if isPrime(self.p):
                break

        while True:
            self.h = getPrime(42)
            self.g = pow(self.h, 2 * self.r, self.p)
            if self.g != 1:
                break

        self.a = randint(2, self.p - 2)
        self.b = randint(2, self.p - 2)

        self.A, self.B = pow(self.g, self.a, self.p), pow(self.g, self.b, self.p)
        self.ss = pow(self.A, self.b, self.p)

    def encrypt(self, flag_part):
        key = sha256(long_to_bytes(self.ss)).digest()[:16]
        cipher = AES.new(key, AES.MODE_ECB)
        ct = cipher.encrypt(pad(flag_part, 16)).hex()
        return f"encrypted = {ct}"

    def get_params(self):
        return f"p = {self.p}\ng = {self.g}\nA = {self.A}\nB = {self.B}"


def menu():
    print("\nChoose as you please\n")
    print("1. Get parameters")
    print("2. Reset parameters!! This can take some time")
    print("3. Get Flag")

    option = input("\n> ")
    return option


def main():
    dh = DH()

    while True:
        choice = int(menu())
        if choice == 1:
            print(dh.get_params())
        elif choice == 2:
            dh.gen_params()
        elif choice == 3:
            print(dh.encrypt(FLAG))
        else:
            print('See you later.')
            exit(1)


if __name__ == "__main__":
    main()
