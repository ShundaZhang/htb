from web3 import Web3
from solcx import compile_files, install_solc

# installs solc compiler, necessary only for first execution
install_solc('0.8.13')

addr = "0x008775247F3098D51e4CC6d2773436a72B01a0B3"
target = "0x14640928E43FA763FF263aD0dBe77cf33E85e3F2"

compiled = compile_files(["Creature.sol"], output_values=["abi"], solc_version="0.8.13")
abi = compiled['Creature.sol:Creature']['abi']


w3 = Web3(Web3.HTTPProvider('http://104.248.166.174:31576/'))
print("current balance", w3.eth.get_balance(addr), "wei")

contract = w3.eth.contract(address=target, abi=abi)

