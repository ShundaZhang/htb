from hashlib import sha256
from pymerkle import InmemoryTree as MerkleTree

root = '3ac45bb080092618726e784297eaa4786cc3681081cfba711fe419d2ab9d8e93'
#sha = ['294ae928b58ee9a33afc678092b9cd170d3ba44420465698b3efa2a2cae18f44', '863b9d58ed87fc846d25f21db463762dff169c581eeb40529cffe600a0b763f0', '10a80be2e7f773ac1fc4bda14db4d43055da273aa58502eb92d3a9df7d6ee82a', 'e3783cf356b70ce14db0fdd79c1d3bcd9a080f6bdb186708941c73b7b876eab3', 'dcd0f22c6400946af1c52c9ba49779400de566a12fbf8553890c9ec62fb0d4f8', '544d4d1c18757688d76046ae1c103e5b1233ef3a428e86a1c121a1cec03afb01', 'a0a8422bb928e34347f906c6c7c4b120c3dac8cdea8b3b74808bedc8a7bd2fe7', '1a76160652995993b3e0472d86c1b808663ab5161dac96999b0ca3a348d11ca0']

sha = ['133b29ca9a6cdd9ef2e20a59bffb5d85a9b62f61deba431bdc7ccea09790ec6a', '82ede2b983aa39469fb080246300922bfc98bb526e4cbee9d3a3aa28097fa78f', '65a295b6def1eb542e320f4f42b2dfdea8265b5b5fc120a27133bf9757719747', '4c6703dea6ddf8bd99f4e07f53a957edb86a148cc7118dfd60cc4e025de2188e', 'abc45876a3fe617f087798d5de77631211bcd3f12f5bd54324226f2a8f044799', '4e96e23f42e0c646e6a30b23c8b077795e32b47e4a96489399ae0de7437ad51d', '392669c8919de0a1c854114318daea0a59bab51fe5b427e52697f5710298de59', '6f8c10606da115fc7ad59ef65d0a29c2b8506e4889f2dbb6b20e1493958f2fb0']

x0 = sha256(bytes.fromhex(sha[0])).digest()+sha256(bytes.fromhex(sha[1])).digest()
x1 = sha256(bytes.fromhex(sha[2])).digest()+sha256(bytes.fromhex(sha[3])).digest()
x2 = sha256(bytes.fromhex(sha[4])).digest()+sha256(bytes.fromhex(sha[5])).digest()
x3 = sha256(bytes.fromhex(sha[6])).digest()+sha256(bytes.fromhex(sha[7])).digest()

print(x0.hex()+','+x1.hex()+','+x2.hex()+','+x3.hex())

'''
mt = MerkleTree(security=False)
mt.append(x0)
mt.append(x1)
mt.append(x2)
mt.append(x3)
print(mt.get_state().hex())
print(root)

_mt = MerkleTree(security=False)
for i in sha:
	_mt.append(bytes.fromhex(i))
print(_mt.get_state().hex())
'''
