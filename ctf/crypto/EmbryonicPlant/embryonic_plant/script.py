from Crypto.Util.number import getPrime, long_to_bytes, inverse
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from hashlib import sha256
from secret import FLAG


class RNG:

    def __init__(self, seed):
        self.e = 0x10001
        self.s = seed

        self.r = getPrime(768)
        while True:
            self.p, self.q = getPrime(768), getPrime(768)
            if self.p < self.r and self.q < self.r:
                break

        self.n = self.p * self.q * self.r
        phi = (self.p - 1) * (self.q - 1) * (self.r - 1)
        self.d = inverse(self.e, phi)

    def next(self):
        self.s = (self.s * self.p + self.q) % self.r
        return self.s


def main():
    rng = RNG(getPrime(512))
    rns = [rng.next() for _ in range(5)]

    key = sha256(long_to_bytes(rng.d)).digest()
    cipher = AES.new(key, AES.MODE_ECB)
    enc_flag = cipher.encrypt(pad(FLAG, 16)).hex()

    with open('output.txt', 'w') as f:
        f.write(f'n = {rng.n}\n')
        f.write(f's = {rns}\n')
        f.write(f'enc_flag = {enc_flag}\n')


if __name__ == "__main__":
    main()
