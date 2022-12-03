ip, port = "167.99.206.87", 30399

from collections import Counter
from pwn import *
import json


def encrypt_oracle(iv, pt):
    io.recvuntil(b'> ')
    payload = json.dumps({"option": "encrypt", "iv": iv.hex(), "pt": pt})
    print(payload)
    io.sendline(payload)
    resp = json.loads(io.recvline().rstrip())
    ct = bytes.fromhex(resp['ct'])
    return ct

def possible_key_bit(key, c):
    s = [i for i in range(256)]
    j = 0
    for i in range(len(key)):
        j = (j + s[i] + key[i]) % 256
        tmp = s[i]
        s[i] = s[j]
        s[j] = tmp

    return (c[0] - j - s[len(key)]) % 256


def attack(key_len):
    key = bytearray([3, 255, 0])
    for a in range(key_len):
        key[0] = a + 3
        possible = Counter()
        for x in range(256):
            key[2] = x
            c = encrypt_oracle(key[:3], b"\x00".hex())
            possible[possible_key_bit(key, c)] += 1
        key.append(possible.most_common(1)[0][0])
    return key[3:]


io = remote(ip, port)
# key = '1fec0787bd1a52ade63a379a203c2be92b981eb117dac4034ecce0'
key = attack(27)
io.recvuntil(b'> ')
io.sendline(json.dumps({"option": "claim", "key": key.hex()}))
print(io.recvline())

