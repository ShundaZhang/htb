from Crypto.Util.number import *
from hashlib import sha1
from Crypto.Cipher import AES

key = 847508536173296595626689
enc_flag = 'df572f57ac514eeee9075bc0ff4d946a80cb16a6e8cd3e1bb686fabe543698dd8f62184060aecff758b29d92ed0e5a315579b47f6963260d5d52b7ba00ac47fd'.decode('hex')

def encrypt(key):
    iv = '\xba\xf9\x13\x7b\x5b\xb8\xfa\x89\x6c\xa8\x4c\xe1\xa9\x8b\x34\xe5'
    key = sha1(str(key).encode('ascii')).digest()[0:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    flag = cipher.decrypt(enc_flag)
    return flag

print encrypt(key)
#HTB{uns4f3_3ll1pt1c_curv3s_l3d_t0_th3_c0ll4ps3_0f_0u7l4nd1s}
