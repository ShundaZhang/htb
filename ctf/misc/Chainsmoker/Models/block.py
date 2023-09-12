import hashlib
import json

from Models.transaction import Transaction

class Block(object):

    def __init__(self, index, timestamp, transactions, proof, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.proof = proof
        self.previous_hash = previous_hash

    def __repr__(self):
        block_string = {"index": self.index, 
                        "timestamp": self.timestamp, 
                        "transaction": [x.json() for x in self.transactions],
                        "proof": self.proof,
                        "previous_hash": self.previous_hash
                        }
        return json.dumps(block_string, sort_keys=True)

    def hash(self):
        hashlib.sha256(str(self).encode()).hexdigest()

    @staticmethod
    def from_json(block):
        transactions = []
        for transaction in block['transactions']:
            tx = Transaction.from_json(transaction)
            transactions.append(tx)
        b = Block(block['index'], block['timestamp'], transactions, block['proof'], block['previous_hash'])
        return b