# uncompyle6 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.7.5 (default, Dec  9 2021, 17:04:37) 
# [GCC 8.4.0]
# Embedded file name: maze.py
import sys, obf_path
ZIPFILE = 'enc_maze.zip'
print('Look who comes to me :)')
print()
inp = input('Now There are two paths from here. Which path will u choose? => ')
if inp == 'Y0u_St1ll_1N_4_M4z3':
    obf_path.obfuscate_route()
else:
    print('Unfortunately, this path leads to a dead end.')
    sys.exit(0)
import pyzipper

def decrypt(file_path, word):
    with pyzipper.AESZipFile(file_path, 'r', compression=(pyzipper.ZIP_LZMA), encryption=(pyzipper.WZ_AES)) as (extracted_zip):
        try:
            extracted_zip.extractall(pwd=word)
        except RuntimeError as ex:
            try:
                try:
                    print(ex)
                finally:
                    ex = None
                    del ex

            finally:
                ex = None
                del ex


decrypt(ZIPFILE, 'Y0u_Ar3_W4lkiNG_t0_Y0uR_D34TH'.encode())
with open('maze', 'rb') as (file):
    content = file.read()
data = bytearray(content)
data = [x for x in data]
key = [0] * len(data)
for i in range(0, len(data), 10):
    data[i] = (data[i] + 80) % 256
else:
    for i in range(0, len(data), 10):
        data[i] = (data[i] ^ key[i % len(key)]) % 256
    else:
        with open('dec_maze', 'wb') as (f):
            for b in data:
                f.write(bytes([b]))
# okay decompiling maze.pyc
