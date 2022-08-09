from Crypto.Util.number import isPrime, getPrime, GCD, long_to_bytes, bytes_to_long
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from secret import flag
from ecc import EllipticCurve
from hashlib import md5
import os
import random
print("Welcome to the ECRSA test center. Your encrypted data will be sent soon.")
print("Please check the logs for the parameters.")
legendre = lambda x,p: pow(x,(p-1)//2,p)
def next_prime(num):
    if num % 2 == 0:
        num += 1
    else:
        num += 2
    while not isPrime(num):
        num += 2
    return num
def getrandpoint(ec,p,q):
    num = random.randint(1,p*q)
    while legendre(expr(num),p) != 1 or legendre(expr(num),q) != 1:
        num = random.randint(1,p*q)
    return ec.lift_x(num,p,q)
# Calculate discriminant(ensures elliptic curve is non-singular)
calc_discrim = lambda a,b,n: (-16 * (4 * a**3 + 27 * b**2)) % n
def keygen(bits):
    # Returns RSA key in form ((e,n),(p,q))
    p = getPrime(bits // 2)
    while p % 4 == 1:
        p = next_prime(p)
    e = next_prime(p >> (bits // 4))
    q = next_prime(p)
    for i in range(50):
        q = next_prime(q)
    while q % 4 == 1:
        q = next_prime(q)
    n = p * q
    if n.bit_length() != bits:
        return keygen(bits)
    return (e,n),(p,q)
print("Generating your key...")
key = keygen(512)
e,n = key[0]
p,q = key[1]
print("Creating ECC params")
# Gotta make sure the params are valid
a,b = random.getrandbits(128),random.getrandbits(128)
discrim = calc_discrim(a,b,n)
expr = lambda x: x**3 + a*x + b
while not discrim:
    a,b = random.getrandbits(128),random.getrandbits(128)
    discrim = calc_discrim(a,b,n)
ec = EllipticCurve(a,b,n)
g = getrandpoint(ec,p,q)
A = ec.multiply(g,e)
# Use key that has been shared with ECRSA
key = md5(str(g.x).encode()).digest()
iv = os.urandom(16)
cipher = AES.new(key,AES.MODE_CBC,iv)
data = cipher.encrypt(pad(flag,16))
print(f"Encrypted flag: {data.hex()}")
print(f"IV: {iv.hex()}")
print(f"N: {n}")
print(f"ECRSA Ciphertext: {A}")
print("Would you like to test the ECRSA curve?")
if input("[y/n]> ") == 'n':
    exit()
print("Generating random point...")
print(getrandpoint(ec,p,q))
print("Thanks for testing!")