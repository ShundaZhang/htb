#!/usr/bin/env python3

import signal
import random, os
from hashlib import sha256
from Crypto.Util.number import isPrime, getPrime, long_to_bytes, bytes_to_long
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from pool import GREET, ANS
from secret import RESTRICTED

class GRAS:
    def __init__(self, m, p, q):
        self.m = m
        self.a = 0xdeadbeef
        self.p = p
        self.q = q

    def generate_key(self):
        ct = 0x1337
        # this loop runs in milliseconds in our super computer
        for _ in range(self.m):
            ct = pow(ct, self.a, self.m)
        return long_to_bytes(ct)[:16]

class OumaraSystem:
    def __init__(self, bits):
        self.BITS = bits
        self.LIMIT = 2
        self.p = getPrime(self.BITS//2)
        self.q = getPrime(self.BITS//2)
        self.N = self.p * self.q
        self.e = 0x10001
        self.d = pow(self.e, -1, (self.p-1)*(self.q-1))
        self.prng = GRAS(self.N, self.p, self.q)

    def encrypt(self, m):
        m = bytes_to_long(m.encode())
        assert 0 < m < self.N
        enc_msg = long_to_bytes(pow(m, self.e, self.N))
        return enc_msg

    def encrypt_plans(self):
        self.symmetric_key = self.prng.generate_key()
        cipher = AES.new(self.symmetric_key, AES.MODE_ECB)
        enc_plans = [cipher.encrypt(pad(r.encode(), 16)) for r in RESTRICTED]
        return enc_plans

    def send_encrypted_message(self, c):
        if c > 1:
            m = pow(c, self.d, self.N)
            try:
                msg = long_to_bytes(m).decode()
                return True
            except:
                pass
        return False

    def reveal_internal_plans(self, encrypted_plans, key):
        cipher = AES.new(key, AES.MODE_ECB)
        plans = [unpad(cipher.decrypt(ep), 16).decode() for ep in encrypted_plans]
        return plans
        
    def hash_verified(self, h):
        return h == sha256(str(self.N).encode()).digest()
    
    def generate_token(self):
        d = self.q.bit_length() - 643
        return ((self.q >> d) << d) | random.getrandbits(d)

def show_banner():
    print('''
   ___                                    ____                              ____ _                            _ 
  / _ \ _   _ _ __ ___   __ _ _ __ __ _  / ___|  ___  ___ _   _ _ __ ___   / ___| |__   __ _ _ __  _ __   ___| |
 | | | | | | | '_ ` _ \ / _` | '__/ _` | \___ \ / _ \/ __| | | | '__/ _ \ | |   | '_ \ / _` | '_ \| '_ \ / _ \ |
 | |_| | |_| | | | | | | (_| | | | (_| |  ___) |  __/ (__| |_| | | |  __/ | |___| | | | (_| | | | | | | |  __/ |
  \___/ \__,_|_| |_| |_|\__,_|_|  \__,_| |____/ \___|\___|\__,_|_|  \___|  \____|_| |_|\__,_|_| |_|_| |_|\___|_|
''')

def menu():
    print('=======================================')
    print('||                                   ||')
    print('||   [S]end your encrypted message   ||')
    print('||   [R]eveal internal plans         ||')
    print('||   [F]orgot decryption key         ||')
    print('||                                   ||')
    print('=======================================')
    return input('> ').upper()[0]

def print_plans(plans):
    print('==================== CLASSIFIED CONTENT! DO NOT SHARE! ====================')
    for i, p in enumerate(plans):
        print(f'Plan {i+1} : {p}')
    print('===========================================================================')


def main():
    crypto = PopperSystem(2048)
    encrypted_plans = crypto.encrypt_plans()

    show_banner()

    print('This channel aims at secure communication via asymmetric encryption.')
    print(f'We say : {crypto.encrypt(random.choice(GREET)).hex()}')

    while True:
        ch = menu()
        if ch == 'S':
            enc_msg = int(input('You say : '), 16)
            verified = crypto.send_encrypted_message(enc_msg)
            if verified:
                print(f'Nice! We say : {crypto.encrypt(random.choice(ANS)).hex()}')
            else:
                print(f'Nice! We say : {os.urandom(256).hex()}')

        elif ch == 'R':
            print('Our plans are encrypted via symmetric encryption and protected with our unique super computer that will take us to the Red Planet!')
            key = bytes.fromhex(input('Enter decryption key : '))
            plans = crypto.reveal_internal_plans(encrypted_plans, key)
            print_plans(plans)
            exit(0)
        
        elif ch == 'F':
            h = bytes.fromhex(input('Before giving you the token, you must prove me that you know the public key : '))
            if crypto.hash_verified(h):
                token = crypto.generate_token()
                print(f'Here is your token : {token}')
                print('Make sure you do not forget it next time!')
            else:
                print('Get out!')

        else:
            print('Hey, this is suspicious! Terminating the channel...')
            exit(0)

if __name__ == '__main__':
    signal.alarm(900)
    main()
