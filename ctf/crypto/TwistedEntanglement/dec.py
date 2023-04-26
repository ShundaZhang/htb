#pip3 install --extra-index-url https://pypi.netsquid.org netsquid

import netsquid as ns
from random import seed, randint
from hashlib import sha256
from Crypto.Cipher import AES

def randomBasis():
    r = randint(0, 1)
    return ns.Z if r else ns.X

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
