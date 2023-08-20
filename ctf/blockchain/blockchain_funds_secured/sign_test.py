from web3 import Web3
from eth_account.messages import encode_defunct
import hashlib

# Connect to an Ethereum node
rpc_url = "http://157.245.37.125:31711"  # Replace with your Ethereum node's URL
w3 = Web3(Web3.HTTPProvider(rpc_url))

# Replace with the private key of the signer
private_key = "0x976bdedb3d2659f6eeb93eff9b5691e645757af37f997ac7036735eead99ff93"

# Addresses from address(1) to address(0xa)
addresses = [w3.to_checksum_address(f"0x{str(i).zfill(40)}") for i in range(1, 0xa)]
Address = "0x7F89D36714adA6e375Da57ce6f6CAcA08CA2a413"

# Hash of the message to be signed
#message_hash = hashlib.sha256(b"Campaign Message").digest()

# Generate signatures for each address
for address in addresses:
    #message_hash = w3.keccak(text="Test Campaign Message "+str(addresses.index(address)))
    message_hash = w3.keccak(text=Address)
    message = encode_defunct(hexstr=w3.to_hex(message_hash))
    signature = w3.eth.account.sign_message(message, private_key=private_key)
    print(signature)
    # Verify the signature and recover the signer's address
    recovered_address = w3.eth.account.recover_message(message, signature=signature.signature)
    #recovered_address = w3.eth.account.recover_message(message, signature=signature.signature[:-10]+b"\x00"*10)
    print(recovered_address)
    
'''
    if recovered_address == address:
        print(f"Signature for {address}:\n- Signature: {signature.signature.hex()}\n- r: {signature.r.hex()}\n- s: {signature.s.hex()}\n- v: {signature.v}")
    else:
        print(f"Signature mismatch for {address}")
'''
