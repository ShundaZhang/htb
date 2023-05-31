from Crypto.Util.number import long_to_bytes, bytes_to_long, getPrime, inverse
import random

FLAG = b'HTB{--REDACTED--}'
p = getPrime(1024)
q = getPrime(1024)
n = p * q
e = 257


def encrypt_flag():
    a = random.getrandbits(1024)
    b = random.getrandbits(1024)

    flag = bytes_to_long(FLAG)

    msg = a*flag + b

    ct = pow(msg, e, n)
    return {'ct': format(ct, 'x'), 'n': format(n, 'x'), 'e': format(e, 'x'), 'a': format(a, 'x'), 'b': format(b, 'x')}
