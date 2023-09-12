import json

class Transaction(object):

    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.data = ""

    def json(self):
        return {"sender": self.sender, "recipient": self.recipient, "amount": self.amount, "data": self.data}

    def __repr__(self):
        tx_string = {"sender": self.sender, "recipient": self.recipient, "amount": self.amount, "data": self.data}
        return json.dumps(tx_string, sort_keys=True)
    
    @staticmethod
    def from_json(transaction):
        tx = Transaction(transaction['sender'], transaction['recipient'], transaction['amount'])
        tx.sig = transaction['sig']
        if "data" in transaction:
            tx.data = transaction['data']
        return tx