#!/usr/bin/env python3

from Crypto.Util.number import *
from secret import flag
import random
import os
def getrandbits(n):
    return bytes_to_long(os.urandom(n // 8))

N = 2**1024

# Generate random key(64-bit number of which 32 of those bits are 1)


key = 0
rem = list(range(64))
for _ in range(32):
    bitpos = random.choice(rem)
    rem.remove(bitpos)
    key |= 1 << bitpos

def doeval(poly, x):
    # Given polynomial and x value, generates y modulo N
    ans = 0
    for i, coeff in enumerate(poly):
        ans += x**i * coeff
        ans %= N
    return ans

def encrypt(msg, key):
    out = ()
    msg = bytes_to_long(msg)
    poly = [msg] + [getrandbits(1024) for _ in range(31)]


    for bitpos in range(64):
        if key & 1 << bitpos != 0:
            # Real
            x = getrandbits(1024)
            out += ((x, doeval(poly, x)),)
        else:
            # Fake
            x = getrandbits(1024)
            y = getrandbits(1024)
            out += ((x,y),)
    return out

def printenc(data, key):
    for pair in encrypt(data, key):
        print(pair)

def menu():
    print("[1]: Get encrypted flag")
    print("[2]: Encrypt your own message")
    return int(input("> "))

doneflagenc = False
try:
    while True:
        try:
            option = menu()
        except:
            print("Invalid menu item")
            continue
        if option == 1:
            if doneflagenc:
                print("Nope")
                continue
            printenc(flag, key)
            doneflagenc = True
        elif option == 2:
            try:
                msg = bytes.fromhex(input("Input message as hex: "))
            except:
                print("Invalid message format")
                continue
            printenc(msg, key)
        else:
            print("Unknown option")
            continue
except:
    print("Unknown error ocurred")
