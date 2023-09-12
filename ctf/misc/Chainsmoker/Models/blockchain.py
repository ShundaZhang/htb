import base64
import hashlib
import json
import os
from time import time
from urllib.parse import urlparse
from uuid import uuid4
from Crypto.PublicKey import RSA
import requests

from Models.BlockchainEncoder import BlockchainEncoder
from Models.block import Block
from Models.transaction import Transaction
from Models.wallet import Wallet

class Blockchain:
    def __init__(self, load=False):
        self.current_transactions = []
        self.chain = []
        self.nodes = []

        if load:
            self.load()
        else:
            # Create the genesis block
            self.new_block(previous_hash='1', proof=100)

    def register_node(self, address):
        """
        Add a new node to the list of nodes

        :param address: Address of node. Eg. 'http://192.168.0.5:5000'
        """

        parsed_url = urlparse(address)
        if parsed_url.netloc:
            self.nodes.append(parsed_url.netloc)
        elif parsed_url.path:
            # Accepts an URL without scheme like '192.168.0.5:5000'.
            self.nodes.append(parsed_url.path)
        else:
            raise ValueError('Invalid URL')


    def valid_chain(self, chain):
        """
        Determine if a given blockchain is valid

        :param chain: A blockchain
        :return: True if valid, False if not
        """

        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            print(f'{last_block}')
            print(f'{block}')
            print("\n-----------\n")
            # Check that the hash of the block is correct
            last_block_hash = last_block.hash()
            if block.previous_hash != last_block_hash:
                return False

            # Check that the Proof of Work is correct
            if not self.valid_proof(last_block.proof, block.proof, last_block_hash):
                return False

            last_block = block
            current_index += 1

        return True

    def resolve_conflicts(self):
        """
        This is our consensus algorithm, it resolves conflicts
        by replacing our chain with the longest one in the network.

        :return: True if our chain was replaced, False if not
        """

        neighbours = self.nodes
        new_chain = None

        # We're only looking for chains longer than ours
        max_length = len(self.chain)

        # Grab and verify the chains from all the nodes in our network
        for node in neighbours:
            response = requests.get(f'http://{node}/chain')

            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

                # Check if the length is longer and the chain is valid
                if length > max_length and self.valid_chain(chain):
                    max_length = length
                    new_chain = chain

        # Replace our chain if we discovered a new, valid chain longer than ours
        if new_chain:
            self.chain = new_chain
            return True

        return False

    def new_block(self, proof, previous_hash):
        """
        Create a new Block in the Blockchain

        :param proof: The proof given by the Proof of Work algorithm
        :param previous_hash: Hash of previous Block
        :return: New Block
        """

        block = Block(
            len(self.chain) + 1, # index
            time(), # timestamp
            self.current_transactions, #transactions
            proof,
            previous_hash or self.hash(self.chain[-1])
        )

        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, tx):
        """
        Creates a new transaction to go into the next mined Block

        :param sender: Address of the Sender
        :param recipient: Address of the Recipient
        :param amount: Amount
        :return: The index of the Block that will hold this transaction
        """
        #tx = Transaction(sender, recipient, amount)

        key = RSA.import_key(base64.b64decode(tx.sender.encode()))

        if not Wallet.verify_message(key, str(tx), tx.sig):
            return -1


        if tx.sender != "0" and self.get_balance(tx.sender, True) < int(tx.amount):
            return -2

        self.current_transactions.append(tx)

        return self.last_block.index + 1

    @property
    def last_block(self):
        return self.chain[-1]

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block

        :param block: Block
        """

        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True, cls=BlockchainEncoder).encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, last_block):
        """
        Simple Proof of Work Algorithm:

         - Find a number p' such that hash(pp') contains leading 4 zeroes
         - Where p is the previous proof, and p' is the new proof
         
        :param last_block: <dict> last Block
        :return: <int>
        """

        last_proof = last_block.proof
        last_hash = last_block.hash()

        proof = 0
        while self.valid_proof(last_proof, proof, last_hash) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof, last_hash):
        """
        Validates the Proof

        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :param last_hash: <str> The hash of the Previous Block
        :return: <bool> True if correct, False if not.

        """

        guess = f'{last_proof}{proof}{last_hash}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def get_nodes(self):
        result = {}
        for block in self.chain:
            for transaction in block.transactions:
                result.setdefault(transaction.sender, 0)
                result.setdefault(transaction.recipient, 0)
                if transaction.sender == "0":
                    result[transaction.recipient] = result[transaction.recipient] + transaction.amount
                else:
                    if result[transaction.sender] - transaction.amount < 0:
                        print("[ERROR] INVALID TRANSACTION DETECTED!")
                    else:
                        result[transaction.recipient] = result[transaction.recipient] + transaction.amount
                        result[transaction.sender] = result[transaction.sender] - transaction.amount
        result.pop("0", "")
        return result

    def get_balance(self, address, pending=False):
        amount = 0
        for block in self.chain:
            for transaction in block.transactions:
                if transaction.sender == address:
                    amount -= transaction.amount
                elif transaction.recipient == address:
                    amount += transaction.amount

        if pending:
            for transaction in self.current_transactions:
                if transaction.sender == address:
                    amount -= transaction.amount
                elif transaction.recipient == address:
                    amount += transaction.amount

        return amount

    def mine(self, tx, proof):

        key = RSA.import_key(base64.b64decode(tx.recipient.encode()))

        try:
            if not Wallet.verify_message(key, str(tx), tx.sig):
                return None
        except:
            print(tx, "\n", tx.sig)
            return None

        last_block = self.last_block
        last_proof = last_block.proof
        last_hash = last_block.hash()

        if self.valid_proof(last_proof, proof, last_hash) is False:
            return None

        self.current_transactions.append(tx)
        previous_hash = last_block.hash()
        return self.new_block(proof, previous_hash)

    def save(self):
        with open("state.json", "w") as f:
            d = json.dumps(self, sort_keys=True, cls=BlockchainEncoder)
            f.write(d)

    def load(self):
        d = None
        with open("state.json") as f:
            d = json.load(f)

        for transaction in d['current_transactions']:
            tx = Transaction.from_json(transaction)
            self.current_transactions.append(tx)

        for nodes in d['nodes']:
            self.nodes.append(nodes)

        for block in d['chain']:
            b = Block.from_json(block)
            self.chain.append(b)
