'''
https://medium.com/hacking-info-sec/how-to-find-images-on-a-block-chain-osint-cde718d0b239
https://edanurbksn.gitbook.io/edanurbksn/writeup/htb-block-hunt3r-write-up

sudo apt-get install -y build-essential
git clone https://github.com/ethereum/go-ethereum
cd go-ethereum
make geth

or download the binary and run directly

geth --goerli

pip install web3

from web3 import Web3
from web3.middleware import geth_poa_middleware
#local clone of the blockchain
w3 = Web3(Web3.IPCProvider('/home/user/.ethereum/goerli/geth.ipc'))
#remote endpoint
#w3 =  Web3(Web3.HTTPProvider('https://goerli.prylabs.net/'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
blockStart = 3100000
blockEnd   = 3155330
for x in range(blockStart,blockEnd):
	block = w3.eth.getBlock(x,True)
	print(block)

> cat image.png | xxd -p|head
89504e470d0a1a0a0000000d4948445200000800000008000806000000b2
a7d330000000017352474200aece1ce900000038655849664d4d002a0000
0008000187690004000000010000001a000000000002a002000400000001
00000800a00300040000000100000800000000009b2e71560000001c6944
4f540000000200000000000004000000002800000400000004000002058b
a646f8fc00004000494441547801ecdd09bca673fd3ffeccd8c6be266b76
a9104989902d91527c2b54284549d6d28a2c21d26289923545a9afa8b408
a5642959921451d9f77d1933f3ffbfdedff2ab34983373ceb93fd77d3f3f
8fc72b4ce7dcf7e77a5eaffbccb9f6e73dcf204080000102040810204080
000102040810204080000102040810204080000102040810204080000102

grep '89504e470d' blocks.txt

cat image-in-hex-merged-parts.txt | xxd -r -p > image.png

'''

from web3 import Web3
from web3.middleware import geth_poa_middleware
w3 = Web3(Web3.IPCProvider('/home/szhan21/.ethereum/goerli/geth.ipc'))
#remote endpoint
#w3 =  Web3(Web3.HTTPProvider('https://goerli.prylabs.net/'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
blockStart = 3142345
blockEnd   = 3142350
for x in range(blockStart,blockEnd):
	block = w3.eth.getBlock(x,True)
	print(block)

#Address 0xb7e53a55da3eea0fbd09566afda143667d77527d, found 2 transactions contains addtional txt info which are actually image data
#Cat the txt to image-in-hex-merged-parts.txt, remove the leading 0 of each txt
#HTB{H4v1ngFuN::W1tH-th3;d0ubl3-edg3d::Sw0Rd$$}
