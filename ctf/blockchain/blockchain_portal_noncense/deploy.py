from web3 import Web3
import rlp

url = 'http://157.245.37.125:30296/rpc'
w3 = Web3(Web3.HTTPProvider(url))

def calculate_contract_address(sender_address, nonce):
    rlp_encoded = rlp.encode([sender_address, nonce])
    contract_address_bytes = w3.keccak(rlp_encoded)[-20:]
    contract_address = contract_address_bytes.hex()
    return contract_address


sender = 0xaDb67e10Fa330db49e98201B4c5F19356CfA3f59
addrs = [0xFC31cde4aCbF2b1d2996a2C7f695E850918e4007,0x598136Fd1B89AeaA9D6825086B6E4cF9ad2BD4cF,0xFc2D16b59Ec482FaF3A8B1ee6E7E4E8D45Ec8bf1]

nonce = 0

while nonce < 65536:
	for j in range(len(addrs)):
		if int(calculate_contract_address(sender, nonce), 16) == addrs[j]:
			print(f'{nonce}:{j}')
	nonce += 1

#130:0
