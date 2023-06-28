import os, json
from hashlib import sha256
from random import randint
from Crypto.Util.number import getPrime, long_to_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from secret import FLAG

class ECC:
    def __init__(self, bits):
        while True:
            self.p = getPrime(bits)
            if self.p % 4 == 3:
                break
        self.a = randint(1, self.p)
        self.b = randint(1, self.p)

    def gen_random_point(self):
        x = randint(2, self.p-2)
        return (x, pow(x**3 + self.a*x + self.b, (self.p+1)//4, self.p))


def menu():
    print("1. Get path parameters")
    print("2. Try to exit the labyrinth")
    option = input("> ")
    return option


def main():
    ec = ECC(512)

    A = ec.gen_random_point()
    print("This is your lucky point:")
    print(json.dumps({'x': hex(A[0]), 'y': hex(A[1])}))

    while True:
        choice = menu()
        if choice == '1':
            r = randint(ec.p.bit_length() // 3, 2 * ec.p.bit_length() // 3)
            print(
                json.dumps({
                    'p': hex(ec.p),
                    'a': hex(ec.a >> r),
                    'b': hex(ec.b >> r)
                }))
        elif choice == '2':
            iv = os.urandom(16)
            key = sha256(long_to_bytes(pow(ec.a, ec.b, ec.p))).digest()[:16]
            cipher = AES.new(key, AES.MODE_CBC, iv)
            flag = pad(FLAG, 16)
            print(
                json.dumps({
                    'iv': iv.hex(),
                    'enc': cipher.encrypt(flag).hex()
                }))
        else:
            print('Bye.')
            exit()


if __name__ == '__main__':
    main()
