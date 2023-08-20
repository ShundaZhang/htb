from pymerkle import InmemoryTree as MerkleTree
from hashlib import sha256
from os import urandom

from secret import FLAG
from utils import *


class Transaction:

    def __init__(self, _from, _to):
        self._from = _from
        self._to = _to
        self._signature = self.getSignature(self._from, self._to)

    def signature(self):
        return self._signature

    def getSignature(self, _from, _to):
        return sha256(_from + _to).digest()


class Block:

    def __init__(self):
        self._transactions = []

    def transactions(self):
        return self._transactions

    def add(self, transaction):
        self._transactions.append(transaction)


class BlockChain:

    def __init__(self):
        self._mined_blocks = []

    def initialize(self):
        for _ in range(3):
            block = Block()
            for _ in range(8):
                transaction = Transaction(urandom(16), urandom(16))
                block.add(transaction)
            self.mine(block)

    def mined_blocks(self):
        return self._mined_blocks

    def size(self):
        return len(self._mined_blocks)

    def mine(self, block):
        self.mt = MerkleTree(security=False)
        for transaction in block.transactions():
            self.mt.append(transaction.signature())

        root_hash = self.mt.get_state()

        self._mined_blocks.append({
            "number": len(self._mined_blocks),
            "transactions": block.transactions(),
            "hash": root_hash.hex()
        })

    def valid(self, _signatures):
        _mt = MerkleTree(security=False)
        for _signature in _signatures:
            _mt.append(_signature)

        if self.mt.get_state() == _mt.get_state():
            return True

        return False


def main():
    blockchain = BlockChain()
    blockchain.initialize()
    mined_blocks = blockchain.mined_blocks()

    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            print_mined_blocks(mined_blocks)
        elif choice == "2":
            # 1. Provide the forged signatures of the last block.
            _signatures = input("Forged transaction signatures: ")

            # 2. Test if the signatures are different from the provided ones.
            signatures = extract_signatures(mined_blocks[-1]["transactions"])
            _signatures = evaluate_signatures(_signatures, signatures)

            # 3. Test if the signatures you gave generate the same root hash.
            if blockchain.valid(_signatures):
                print(FLAG)
                exit(0)
            else:
                print("Try again")
        else:
            print("Good Bye")
            exit(0)


if __name__ == "__main__":
    main()
