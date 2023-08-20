def menu():
    print("[1] Explore mined blocks")
    print("[2] Forge the last block")


def extract_signatures(transactions):
    return [transaction.signature() for transaction in transactions]


def hexify(elements):
    return [element.hex() for element in elements]


def unhexify(elements):
    return [bytes.fromhex(element) for element in elements]


def print_mined_blocks(mined_blocks):
    for block in mined_blocks:
        print(f"Block: {block['number']}")
        print(f"Hash: {block['hash']}")
        print(
            f"Transactions: {hexify(extract_signatures(block['transactions']))}"
        )
        print()


def evaluate_signatures(_signatures, signatures):
    try:
        _signatures = _signatures.split(",")
        _signatures = unhexify(_signatures)
        if _signatures == signatures:
            print(f"Signatures are the same.")
            exit(0)
    except Exception as e:
        print(f"Something went wrong {e}")
        exit(0)

    return _signatures
