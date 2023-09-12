import json

class BlockchainEncoder(json.JSONEncoder):
        def default(self, o):
            return o.__dict__