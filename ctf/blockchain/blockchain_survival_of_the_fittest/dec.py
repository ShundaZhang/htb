from web3 import Web3
import json
from web3.gas_strategies.rpc import rpc_gas_price_strategy

PrivateKey = "0x5351b3054b36550274478640a950191ca28632b2d76d8f1b4b067b8e3fca40ae"
Address = "0x008775247F3098D51e4CC6d2773436a72B01a0B3"
TargetAddress = "0x14640928E43FA763FF263aD0dBe77cf33E85e3F2"
setupAddress =  "0x5f102976998c981fB4A5730E2AC73FD4e09cd2D7"

url = 'http://104.248.166.174:31576'

w3 = Web3(Web3.HTTPProvider(url))
#block_number = w3.eth.block_number
#print(block_number)

account_address = Address
balance = w3.eth.get_balance(account_address)
#print(balance)

