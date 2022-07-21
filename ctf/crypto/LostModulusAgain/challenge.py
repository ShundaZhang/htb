#!/usr/bin/python3
from Crypto.Util.number import getPrime, long_to_bytes, inverse
from os import urandom

flag = open('flag.txt', 'r').read().strip().encode()
class RSA:
    def __init__(self):
        self.p = getPrime(1024)
        self.q = getPrime(1024)
        self.e = 3
        self.n = self.p * self.q
        self.d = inverse(self.e, (self.p-1)*(self.q-1))
    def encrypt(self, data: bytes) -> bytes:
        pt = int(data.hex(), 16)
        ct = pow(pt, self.e, self.n)
        return long_to_bytes(ct)
    def decrypt(self, data: bytes) -> bytes:
        ct = int(data.hex(), 16)
        pt = pow(ct, self.d, self.n)
        return long_to_bytes(pt)

def main():
    #padding makes everything secure :lemonthink:
    def pad(data: bytes) -> bytes:
        return data+urandom(16)
    crypto = RSA()
    print ('Flag1 :', crypto.encrypt(pad(flag)).hex())
    print ('Flag2 :', crypto.encrypt(pad(flag)).hex())
    print( 'msg1 :', crypto.encrypt(b"Lost modulus had a serious falw in it , we fixed it in this version, This should be secure").hex())
    print( 'msg2 :', crypto.encrypt(b"If you can't see the modulus you cannot break the rsa , even my primes are 1024 bits , right ?").hex())
if __name__ == '__main__':
    main()