'''
This is your lucky point:
{"x": "0x22c317eecf1799f74facf0c5b47aee31479b073d33900b976710f3d523d8ffed9cb3e27c2cb67f06877a9485ff6e7277981d45069330edbca3de929f6ac1f363", "y": "0xc08a052f2c56484ee1be80f5b26bd42d8389c0a24039c5db12c2f88da225b631797695f2aff5d9de8684550f16f7a189a9b61f1cb3337420e148040b55555bbc"}
1. Get path parameters
2. Try to exit the labyrinth
> 1
{"p": "0xda2c5dde59d6534498abb2897cc21fe6910c9a29ca0b1341cecd586e99afc049fe15bf6743756e54766e8c75e1708b6335b6332153d84d3d060958b2a155f44f", "a": "0x67d252d9c16a0a000a07618ba69c6ac490b354b33ee3174d605ddcdc3d6df9e81878", "b": "0x270abb04095c001e68aafb4bf9dc9703397464595b9b544192be4fcf5fd55bd7ea5fc"}
1. Get path parameters
2. Try to exit the labyrinth
> 2
{"iv": "bf95195b7964c37857ec381e6d4bd641", "enc": "bfb4636de908ffea6e68beb8c089f079260e2588bfbd1e202a2e376bc028148083f8d86917676d4f8ecc55547b93b1387e79e0254237106faa36b350baa54372"}
'''

#https://chovid99.github.io/posts/cyber-apocalypse-2023-crypto/#elliptic-labyrinth-revenge
#https://github.com/defund/coppersmith

'''
f(x) = x^3 - y^2 + (partial_a*2^r + c)*x + (partial_b*2^r + d) mod p
c and d is small, r is bruteforceable
bounds = [2^r, 2^r]
'''

#from dec.sage
a = 1359394296266259783582881407859733795057253604466976290157314381815148679766421622671042830587917285320243505101412266095848841356888126527515300967264492 
b = 8179164261619415504071605194854386621945869655260983023535579932334876145224273804403565020082627541823627915038918581819045591908033481663243830523226933 
p = 0xda2c5dde59d6534498abb2897cc21fe6910c9a29ca0b1341cecd586e99afc049fe15bf6743756e54766e8c75e1708b6335b6332153d84d3d060958b2a155f44f

from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes

iv = bytes.fromhex('cb0eae6f4c2dec2af9f93c19313ab9bb')
enc = bytes.fromhex('02af57bc1c9fa4e46e76f0251d67d962b5ea78480fea90832f4f22d8f5229539441bb6d49bf16eeac6cbde47bcb6bc095f0d501731c24fcb9d7ae985fc6f6bed')

key = sha256(long_to_bytes(pow(a, b, p))).digest()[:16]
cipher = AES.new(key, AES.MODE_CBC, iv)

print(cipher.decrypt(enc))
#b'HTB{w3_h0p3_th1s_0n3_h3lp3d_y0u_und3rst4nd_sm411_r00ts}\t\t\t\t\t\t\t\t\t'
