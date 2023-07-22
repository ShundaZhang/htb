from web3 import Web3
import json
from web3.gas_strategies.rpc import rpc_gas_price_strategy
from solcx import compile_source, install_solc, compile_files

x = {
    "PrivateKey": "0xd784c3254bb14442f7048fdca79635a9ce22aa319c0f21f2c25d6d75e3cb5008",
    "Address": "0x6b2D5Ccae6393C0a2902f47d71CDBD7ccBC2E8AB",
    "TargetAddress": "0x78a595485a155f595b22f727cC657cb90279698a",
    "setupAddress": "0x0B73F6DeF9EC18495Af5A51f676aab70D23BaD11"
}

PrivateKey =    x["PrivateKey"]
Address =       x["Address"] 
TargetContract = x["TargetAddress"]
SetupContract =  x["setupAddress"]

url = 'http://143.110.169.131:32371/rpc'

w3 = Web3(Web3.HTTPProvider(url))
block_number = w3.eth.block_number
print(block_number)

account_address = Address
balance = w3.eth.get_balance(account_address)
print(balance)

install_solc("0.8.13")

compiled = compile_files(["Rivals.sol"], output_values=["abi"], solc_version="0.8.13")
abi = compiled['Rivals.sol:Rivals']['abi']

key = bytes.fromhex(PrivateKey[2:])

contract_instance2 = w3.eth.contract(address=TargetContract, abi=abi)
construct_txn = contract_instance2.functions.talk(key).transact()

compiled = compile_files(["Setup.sol"], output_values=["abi"], solc_version="0.8.13")
abi = compiled['Setup.sol:Setup']['abi']

contract_instance = w3.eth.contract(address=SetupContract, abi=abi)
number = contract_instance.functions.isSolved(account_address).call()

print(f'The current number stored is: { number } ')
#
