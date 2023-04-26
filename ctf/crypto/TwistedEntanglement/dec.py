#pip3 install --extra-index-url https://pypi.netsquid.org netsquid

import netsquid as ns
from random import seed, randint
from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Util.number import *

def randomBasis():
    r = randint(0, 1)
    return ns.Z if r else ns.X

def bitsToHash(bits):
    bit_string = ''.join([str(i) for i in bits])
    blocks = bytes(
        [int(bit_string[i:i + 8], 2) for i in range(0, len(bit_string), 8)])
    return sha256(blocks).digest()

private_key = 3262827136301000405966
seed(private_key)
server_basis = ''
for i in range(256):
	b = randomBasis()
	if b == ns.Z:
		server_basis += 'Z'
	else:
		server_basis += 'X'

print(server_basis)

'''
nc 161.35.36.167 30592
Public Key: [89907504838098176881263441878802964785728583665548783922776295846870720845480, 10910183367736376886887663612263638465534220103422068463354807740371827004190]

|---------------------------------------|
| Welcome to Twisted Entanglement!      |
| Maybe we can change the Crypto world  |
| with a physical phenomena :D          |
|---------------------------------------|
| [1] Test our SuperMegaHyperSecure     |
|     Elliptic Curve ;)                 |
| [2] Play with our Qubits ^__^         |
| [3] Abort Mission X__X                |
|---------------------------------------|

> 2

Choose your 256 basis for the KEP: ZZZXXZZZXXXXXXXZXZXXZXXXZXXZZXZZXXXXXXXXZZXXXZXXZZXXZZZZZZZZXXXXZXXZZXZZXZZXXZXZXXXZZZXXXXXXZXXXZXZXXXXXZZXZZZXXXZXZXXXXXXXXZXXZXZZXZXXZXZZXXZZXZZXXZXXXZZZZXZZXXZXXXXXZXZXXZZZZZZZXXZZXZZXXXZZXXZXZZXXXZZZZXZZXXZZZZZXXXXXZXZXXZXZZXXXXXXXZXXZZZZZXZXXXXZXXXZXX

The Quantum key: 79c43889a09623ea819a688c7a65f485ef9064a6848bf1cafea34848a690dd55
Flag Encrypted: 26d23eb4cc776990a92813988f00f16cfd5f494d7c5cc180bce8550c38757125ea9f4cada1003f9de3c6599a3d3b8dfea35c730a644016f7602d3945247295369f8cb347c3526eae41e5484a6e15ca66
'''

q_user_key = 0x79c43889a09623ea819a688c7a65f485ef9064a6848bf1cafea34848a690dd55

key_bytes = long_to_bytes(q_user_key)

bits = []
for byte in key_bytes:
	s = bin(int(byte))[2:].zfill(8)
	for i in s:
		bits.append(int(i))

server_bits = []
for i in bits:
	if i == 0:
		server_bits.append(1)
	else:
		server_bits.append(0)

q_server_key = bitsToHash(server_bits)
#print(q_server_key)

c = bytes.fromhex('26d23eb4cc776990a92813988f00f16cfd5f494d7c5cc180bce8550c38757125ea9f4cada1003f9de3c6599a3d3b8dfea35c730a644016f7602d3945247295369f8cb347c3526eae41e5484a6e15ca66')
cipher = AES.new(q_server_key, AES.MODE_ECB)
flag = cipher.decrypt(c)
print(flag)
#b'HTB{Ek3rT_W4s_s000_b0R1nG_1N_1991_4nD_1_h4t3_Pr0b4b1l1Ty_s0_I_Us3_4_ECC_S33d!}\x02\x02'
