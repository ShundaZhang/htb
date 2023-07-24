from web3 import Web3
import json
from web3.gas_strategies.rpc import rpc_gas_price_strategy
from solcx import compile_source, install_solc, compile_files

x = {
    "PrivateKey": "0x83ffaa8bbe7c0b30f83264d84094097700ab9267ad12f4dfd30881da825fd43c",
    "Address": "0x0C54eD36684B7520945d64f7F63336f96fa1eCc6",
    "TargetAddress": "0x91e13CcFF3cdC5B2Ae9a86aDC5d5D6c8609c260f",
    "setupAddress": "0x7a5aB50d83b0C0D995fa383FC1d001aF90824c92"
}

PrivateKey =    x["PrivateKey"]
Address =       x["Address"] 
TargetContract = x["TargetAddress"]
SetupContract =  x["setupAddress"]

url = 'http://144.126.206.249:31429/rpc'

w3 = Web3(Web3.HTTPProvider(url))
chain_id = w3.eth.chain_id
print(chain_id)
account = w3.eth.accounts
print(account)
block_number = w3.eth.block_number
print(block_number)

account_address = Address
balance = w3.eth.get_balance(account_address)
print(balance)

install_solc("0.8.13")

compiled = compile_files(["Rivals.sol"], output_values=["abi"], solc_version="0.8.13")
abi = compiled['Rivals.sol:Rivals']['abi']

#key = bytes.fromhex(PrivateKey[2:])
key = b'\x00'*32

contract_instance2 = w3.eth.contract(address=TargetContract, abi=abi)
construct_txn = contract_instance2.functions.talk(key).transact()

compiled = compile_files(["Setup.sol"], output_values=["abi"], solc_version="0.8.13")
abi = compiled['Setup.sol:Setup']['abi']

contract_instance = w3.eth.contract(address=SetupContract, abi=abi)
number = contract_instance.functions.isSolved(account_address).call()

print(f'The current number stored is: { number } ')
#
