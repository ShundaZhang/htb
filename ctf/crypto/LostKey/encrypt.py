#!/usr/bin/env python3
from Crypto.Util.number import *
from hashlib import sha1
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from secret import flag, n

class coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"coord({self.x}, {self.y})"

class EC:
    def __init__(self, p):
        self.p = p
        self.zero = coord(0,0)

    def add(self, P,Q):
        if P == self.zero:
            return Q
        if Q == self.zero:
            return P
        if P.x == Q.x and P.y == -Q.y:
            return self.zero
        if P != Q:
            Lambda = (Q.y - P.y) * inverse(Q.x - P.x, self.p)
        else:
            Lambda = (3*(P.x*Q.x) + 417826948860567519876089769167830531934*P.x + 177776968102066079765540960971192211603) * inverse(P.y+Q.y+3045783791, self.p)
        Lambda %= self.p
        R = coord(0,0)
        R.x = (Lambda**2-P.x-Q.x-208913474430283759938044884583915265967) % self.p
        R.y = (Lambda*(P.x-R.x) - P.y - 3045783791) % self.p
        return R

    def mul(self, P, n):
        Q = P
        R = self.zero
        while n > 0:
            if n % 2 == 1:
                R = self.add(R,Q)
            n >>= 1
            Q = self.add(Q,Q)
        return R

def encrypt(key):
    iv = __import__('os').urandom(16)
    key = sha1(str(key).encode('ascii')).digest()[0:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ct = cipher.encrypt(pad(flag,16))
    return(ct.hex(),iv.hex())

assert(n < 38685626227668133590597631)
e = EC(101177610013690114367644862496650410682060315507552683976670417670408764432851)
G = coord(14374457579818477622328740718059855487576640954098578940171165283141210916477, 97329024367170116249091206808639646539802948165666798870051500045258465236698)

print ("G =",G)
print ("Gn =", e.mul(G,n).x)
enc = encrypt(n)
print ("Ciphertext: {}\nIV: {}".format(enc[0],enc[1]))
