from web3 import Web3
from eth_account.messages import encode_defunct
import hashlib

# Connect to an Ethereum node
rpc_url = "http://157.245.37.125:32675"  # Replace with your Ethereum node's URL
web3 = Web3(Web3.HTTPProvider(rpc_url))

# Replace with the private key of the signer
private_key = "0x44134c9e9a818985a3d101beb99cecb3070e888e5b84273947f30039dce82517"

# Addresses from address(1) to address(0xa)
addresses = [web3.toChecksumAddress(f"0x{str(i).zfill(40)}") for i in range(1, 0xb)]

# Hash of the message to be signed
message_hash = hashlib.sha256(b"Campaign Message").digest()

# Generate signatures for each address
for address in addresses:
    message = encode_defunct(hexstr=Web3.toHex(message_hash))
    signature = web3.eth.account.sign_message(message, private_key=private_key)

    # Verify the signature and recover the signer's address
    recovered_address = web3.eth.account.recover_message(message, signature=signature.signature)
    
    if recovered_address == address:
        print(f"Signature for {address}:\n- Signature: {signature.signature.hex()}\n- r: {signature.r.hex()}\n- s: {signature.s.hex()}\n- v: {signature.v}")
    else:
        print(f"Signature mismatch for {address}")

