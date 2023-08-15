from web3 import Web3
from solcx import compile_files

# Connect to an Ethereum node
rpc_url = "http://157.245.43.189:31383/rpc"  # Replace with your Ethereum node's URL
web3 = Web3(Web3.HTTPProvider(rpc_url))

# Replace with your private key
private_key = "0x2de3d450f2b9f28d5640560572511a56b1133ff1f39236fc40e51c6fb55e945c"
sender_addr = "0xaDb67e10Fa330db49e98201B4c5F19356CfA3f59"

compiled = compile_files(["Contract.sol"], output_values=["abi"], solc_version="0.8.13")
compiled_bin = compile_files(["Contract.sol"], output_values=["bin"], solc_version="0.8.13")

abi = compiled["Contract.sol:Contract"]["abi"]
bytecode = compiled_bin["Contract.sol:Contract"]["bin"]

# Set the nonce value
nonce = web3.eth.get_transaction_count(web3.eth.accounts[0])
#nonce = 130
print(f'nonce = {nonce}')

Incrementer = web3.eth.contract(abi=abi, bytecode=bytecode)
construct_txn = Incrementer.constructor().build_transaction(
    {
        'from': sender_addr,
	"gasPrice": web3.to_wei(50, 'gwei'),
	"gas": 21000,
        'nonce': nonce
    }
)

# Sign the transaction
signed_txn = web3.eth.account.sign_transaction(construct_txn, private_key)

# Send the transaction
tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

contract_address = tx_receipt["contractAddress"]
print(f"Contract deployed at address: {contract_address}")

