from web3 import Web3
from solcx import compile_files
from web3.middleware import geth_poa_middleware

# Connect to an Ethereum node
rpc_url = "http://157.245.43.189:32252/rpc"  # Replace with your Ethereum node's URL
web3 = Web3(Web3.HTTPProvider(rpc_url))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Replace with your private key
private_key = "0x2de3d450f2b9f28d5640560572511a56b1133ff1f39236fc40e51c6fb55e945c"

compiled = compile_files(["Contract.sol"], output_values=["bin"], solc_version="0.8.13")

contract_interface = compiled["Contract.sol:Contract"]

# Set the nonce value
#nonce = web3.eth.getTransactionCount(web3.eth.accounts[0])
nonce = 130
# Build the transaction
transaction = {
    "nonce": nonce,
    "gasPrice": web3.to_wei("20", "gwei"),
    "gas": 2000000,
    "to": "",
    "data": contract_interface["bin"],
    #"chainId": 1,  # Mainnet
}

# Sign the transaction
signed_txn = web3.eth.account.sign_transaction(transaction, private_key)

# Send the transaction
tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

contract_address = tx_receipt["contractAddress"]
print(f"Contract deployed at address: {contract_address}")

