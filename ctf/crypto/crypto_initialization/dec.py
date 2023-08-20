#!/usr/bin/env python3

import os
from Crypto.Util import Counter
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
from pwn import *

msg = 'This is some public information that can be read out loud.'
msg1 = pad(msg.encode(), 16)

c1 = bytes.fromhex('2ac199d1395745812e3e5d3c4dc995cd2f2a076426b70fd5209cdd5ddc0a0c372feb3909956a791702180f591a63af184c27a6ba2fd61c1741ea0818142d0b92')
c2 = bytes.fromhex('36fdb2d97d0a5bcf0225586a1e8abfc62d3057273aab5ae5309d8c4ade060a236aed070d817b2c14110e590b1b27ef5d4d35ddc001b47d6c2bca00101c25039a')
ks = xor(msg1,c1)
flag = xor(ks,c2)
print(flag)
