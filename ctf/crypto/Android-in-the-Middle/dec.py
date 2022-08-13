from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes
import hashlib

def decrypt(encrypted, shared_secret):
    key = hashlib.md5(long_to_bytes(shared_secret)).digest()
    cipher = AES.new(key, AES.MODE_ECB)
    message = cipher.decrypt(encrypted)
    return message

def encrypt(encrypted, shared_secret):
    key = hashlib.md5(long_to_bytes(shared_secret)).digest()
    cipher = AES.new(key, AES.MODE_ECB)
    message = cipher.encrypt(encrypted)
    return message


encrypted = 'Initialization Sequence - Code 0'
shared_secret = 1

s = encrypt(encrypted,shared_secret).encode('hex')
print s
s = s.decode('hex')
print decrypt(s,shared_secret)

#HTB{7h15_15_cr3@t3d_by_Danb3er_@nd_h@s_c0pyr1gh7_1aws!_!}
