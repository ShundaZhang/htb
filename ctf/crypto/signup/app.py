from Crypto.Util.number import getPrime, getRandomRange, isPrime, inverse, long_to_bytes, bytes_to_long
from hashlib import sha512
from random import SystemRandom
from FLAG import flag

L = 2048
N = 256

def repeating_xor_key(message, key):

    repeation = 1 + (len(message) // len(key))
    key = key * repeation
    key = key[:len(message)]
    
    msg = bytes([c ^ k for c, k in zip(message, key)])
    return msg

def domain_params_generation():

    q = getPrime(N)

    print(f"[+] q condition is satisfied : {N} bit")
    print(q)

    p = 0
    while not (isPrime(p) and len(bin(p)[2:]) == L):
        factor = getRandomRange(2**(L-N-1), 2**(L-N))
        p = factor*q + 1
        
    print(f"[+] p condition is satisfied : {L} bit")
    print(p)

    g = 1
    while g == 1:
        h = getRandomRange(2, p-2)
        g = pow(h, factor, p)

    print(f"[+] g condition is satisfied ")
    print(g)

    
    return(p, q, g)


def key_generation(p, q, g):

    x = getRandomRange(1, q-1)
    y = pow(g, x, p)

    # print(f"[+] private key : {x}")
    print(f"[+] public key  : {y}")

    return(x, y)


def sign(message, private_key, parameters):

    p, q, g = parameters
    k = getRandomRange(1, q-1)

    r = 0
    while r == 0:
        r = pow(g, k, p) % q

    s = 0
    while s == 0:
        Hm = int(sha512(message.encode('utf-8')).hexdigest(), 16)
        s = (inverse(k, q) * (Hm + private_key*r)) % q

    return (r, s)


def verify(message, signature, public_key, parameters):

    p, q, g = parameters
    r, s = signature

    if 0 < r < q and 0 < s < q:
        
        w = inverse(s, q)
        Hm = int(sha512(message.encode('utf-8')).hexdigest(), 16)
        u1 = (Hm * w) % q
        u2 = (r * w) % q
        v = ( (pow(g, u1, p) * pow(public_key, u2, p)) % p ) % q

        if v == r:
            print(f"[+] Valid signature")
            return True
        else:
            print("[!] Invalid signature")
            return False


parameters = domain_params_generation()
p, q, g = parameters

keys = key_generation(p, q, g)
x, y = keys

print()
print("=============================================================================================")
print("===================================== Let's signup ==========================================")
print("=============================================================================================")
print()

with open('./messages', 'r') as o:

    messages = o.readlines()

    for message in messages:
        
        message = message.rstrip()
        print("********************************************************************************")
        print(f"message : {message}")
        signature = sign(message, x, parameters)
        r, s = signature
        print(f"signature: {signature}")

        # verify(message, signature, y, parameters)

    o.close()


key = long_to_bytes(x)
ctf = repeating_xor_key(flag, key)
print()
print("[+] Cipher Text Flag (CTF) : ")
print(hex(bytes_to_long(ctf))[2:])