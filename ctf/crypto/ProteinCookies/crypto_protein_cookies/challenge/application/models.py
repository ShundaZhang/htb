import hashlib, base64, urlparse, os

secret = os.urandom(16)

class session:
    @staticmethod
    def create(username, logged_in='True'):
        if username == 'guest':
            logged_in = 'False'

        hashing_input = 'username={}&isLoggedIn={}'.format(username, logged_in)
        crypto_segment = signature.create(hashing_input)
        
        return '{}.{}'.format(signature.encode(hashing_input), crypto_segment)
    
    @staticmethod
    def validate_login(payload):
        hashing_input, crypto_segment = payload.split('.')

        if signature.integrity(hashing_input, crypto_segment):
            return {
                k: v[-1] for k, v in urlparse.parse_qs(signature.decode(hashing_input)).items()
            }.get('isLoggedIn', '') == 'True'
        
        return False

class signature:
    @staticmethod
    def encode(data):
        return base64.b64encode(data)

    @staticmethod
    def decode(data):
        return base64.b64decode(data)

    @staticmethod
    def create(payload, secret=secret):
        return signature.encode(hashlib.sha512(secret + payload).hexdigest())
    
    @staticmethod
    def integrity(hashing_input, crypto_segment):
        return signature.create(signature.decode(hashing_input)) == crypto_segment