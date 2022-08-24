from Crypto.Util.number import bytes_to_long, long_to_bytes, inverse
from base64 import b64encode, b64decode
import random


class ElGamal:
    def __init__(self):
        self.g = 10
        self.q = 855098176053225973412431085960229957742579395452812393691307482513933863589834014555492084425723928938458815455293344705952604659276623264708067070331
        self.h = 503261725767163645816647683654078455498654844869971762391249577031304598398963627308520614235127555024152461204399730504489081405546606977229017057765
        self.s = None
        self.y = random.randint(2, self.q)

    # This was used for self.h generation
    def generateKey(self) -> int:
        x = random.randint(2, self.q)
        return pow(self.g, x, self.q)

    def encrypt(self, m: int) -> str:
        s = pow(self.h, self.y, self.q)
        c1 = pow(self.g, self.y, self.q)
        c2 = (s * m) % self.q
        c1 = b64encode(long_to_bytes(c1)).decode()
        c2 = b64encode(long_to_bytes(c2)).decode()
        return c1 + "|" + c2

    def decrypt(self, ct: str) -> str:
        c1, c2 = ct.split("|")
        c1 = bytes_to_long(b64decode(c1))
        c2 = bytes_to_long(b64decode(c2))
        s = pow(c1, self.y, self.q)
        s = pow(self.h, self.y, self.q)
        m = (c2 * inverse(s, self.q)) % self.q
        return long_to_bytes(m)
