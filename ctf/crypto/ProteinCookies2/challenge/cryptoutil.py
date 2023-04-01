from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

BLOCK_LEN = 32
SECRET = get_random_bytes(50)

iv = b"@\xab\x97\xca\x18\x1d\xac<\x1e\xc3xC\x9b\x1c\xc5\x1f\x8aD=\xec*\x16G\xe7\x89'\x80\xe4\xe6\xfc5l"


def pad(data):
    if len(data) % BLOCK_LEN == 0:
        return data

    pad_byte = bytes([len(data) % 256])
    pad_len = BLOCK_LEN - (len(data) % BLOCK_LEN)
    data += pad_byte * pad_len

    return data


def compression_function(data, key):
    if len(data) != BLOCK_LEN or len(key) != BLOCK_LEN:
        raise ValueError(f"Input for compression function is not {BLOCK_LEN} bytes long!")

    # AES is a safe compression function, right? Why not just use that?
    cipher = AES.new(key, AES.MODE_ECB)
    enc = cipher.encrypt(data)

    # let's confuse it up a bit more, don't want to make it too easy!
    enc = enc[::-1]
    enc = enc[::2] + enc[1::2]
    enc = enc[::3] + enc[2::3] + enc[1::3]

    return enc


def lj12_hash(data):
    data = pad(data)

    blocks = [data[x:x + BLOCK_LEN] for x in range(0, len(data), BLOCK_LEN)]
    enc_block = iv

    for i in range(len(blocks)):
        enc_block = compression_function(blocks[i], enc_block)

    return enc_block.hex()
