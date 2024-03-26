from hashlib import sha256
import string, random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import b64decode

'''
Your Password : t*!zGnf#LKO~drVQc@n%oFFZyvhvGZq8zbfXKvE1#*R%uh*$M6c$zrxWedrAENFJB7xz0ps4zh94EwZOnVT9&h
Encrypted Flag : GKLlVVw9uz/QzqKiBPAvdLA+QyRqyctsPJ/tx8Ac2hIUl8/kJaEvHthHUuwFDRCs
'''

ALPHABET = string.ascii_letters + string.digits + '~!@#$%^&*'

def generate_password():
    master_key = int.from_bytes(MASTER_KEY, 'little')
    password = ''

    while master_key:
        bit = master_key & 1
        if bit:
            password += random.choice(ALPHABET[:len(ALPHABET)//2])
        else:
            password += random.choice(ALPHABET[len(ALPHABET)//2:])
        master_key >>= 1

    return password

def recovery(password):
    master_key = ''
    for c in password:
        if c in ALPHABET[:len(ALPHABET)//2]:
            master_key += '1'
        elif c in ALPHABET[len(ALPHABET)//2:]:
            master_key += '0'
    return master_key[::-1]

password = 't*!zGnf#LKO~drVQc@n%oFFZyvhvGZq8zbfXKvE1#*R%uh*$M6c$zrxWedrAENFJB7xz0ps4zh94EwZOnVT9&h'

master_key = int(recovery(password),2)
print(master_key)

byte_order = 'little'  
byte_length = (master_key.bit_length() + 7) // 8

MASTER_KEY = master_key.to_bytes(byte_length, byte_order)

print(MASTER_KEY)
master_key = int.from_bytes(MASTER_KEY, 'little')
print(master_key)

encryption_key = sha256(MASTER_KEY).digest()
cipher = AES.new(encryption_key, AES.MODE_ECB)
ct = b64decode('GKLlVVw9uz/QzqKiBPAvdLA+QyRqyctsPJ/tx8Ac2hIUl8/kJaEvHthHUuwFDRCs')
print(cipher.decrypt(ct))
