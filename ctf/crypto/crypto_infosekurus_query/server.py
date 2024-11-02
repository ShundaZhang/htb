from Crypto.Util.number import GCD, long_to_bytes as l2b, bytes_to_long as b2l
from secret import FLAG, passwords, moduli, hash_word, tfa_questions
import json, os, random
from Crypto.Cipher import AES
from hashlib import md5

exponents = [65537, 4001, 11093, 7727, 32189, 19373, 8192, 7867, 599741, 919, 3697, 227, 9613]

class Generator:
    def __init__(self):
        self.passcode = random.choice(passwords)
        self.pool = "+%2$?!_8*4"
        self.mods = moduli
        
    def encrypt(self, choice):
        p, q = self.mods[choice]
        self.N = p * q
        self.e = exponents[choice]
        self.phi = (p-1)*(q-1)
        # what?! o.O
        if GCD(self.phi, self.e) == 1:
            self.phi = None
        ciphertext = pow(b2l(self.passcode), self.e, self.N)
        return ciphertext
    
    def rxor(self, x):
        r = b''.join(l2b(random.choice(x)) for _ in range(10))
        idx = 0
        while len(r) != len(x):
            r += l2b(r[idx % len(r)])
            idx += 1
        r2 = b2l(os.urandom(len(x))) & (1<<(8*len(x))-1) 
        return l2b(b2l(r) & r2) * len(x)
    
    def randomize(self, password):
        for c in "abcdef01357":
            password = password.replace(c, random.choice(self.pool))
        return ''.join(random.choices(password, k=5))
    
class Hasher:
    def __init__(self, key):
        self.key = key
        self.extra = md5(hash_word).digest()

    # a xor b
    def bxor(self, a, b):
        return bytes(x ^ y for x, y in zip(a, b))

    # left rotate a by b bits
    def blshift(self, a, b):
        return bytes((((x % 2**((8-y)%8)) << y) | (x >> ((8-y)%8))) & 0xff for x, y in zip(a, b))
    
    def pad(self, message):
        bit_bytes = (8 * len(message)) & 0xffffffffffffffff
        message += b"\x80"
        while len(message) % 32 != 28:
            message += b"\x00"
        message += bit_bytes.to_bytes(4, byteorder='big')
        return message

    def hash_digest(self, message):
        to_hash = self.pad(self.key + self.extra + message)
        seed = b"\xff" * 16
        blocks = [b"\xfe" * 16] + [to_hash[i:i+16] for i in range(0, len(to_hash), 16)]
        for b in range(1, len(blocks)):
            cipher = AES.new(blocks[b], AES.MODE_ECB)
            seed = self.bxor(cipher.encrypt(self.blshift(seed, blocks[b-1])), seed)
        return seed
        
    def two_factor_generate(self, message, answer, randomized):
        if not answer:
            answer = os.urandom(16)
        randomized = self.pad(randomized.encode())
        token = self.hash_digest(message + answer + randomized[-16:] + randomized[:16])
        return randomized[:5], token

def get_option():
    return input('''
    === Options ===
    [1] Encrypted Passcode
    [2] Hash
    [3] Authenticate
    [4] Exit

        Option (json format) :: ''')

def main():
    print("""
     █████████                                                      █████████                      █████                                ██████████     █████████   ██████   ██████     ████████     █████       █████       █████   
    ███░░░░░███                                                    ███░░░░░███                    ░░███                                ░░███░░░░███   ███░░░░░███ ░░██████ ██████     ███░░░░███  ███░░░███   ███░░░███   ███░░░███ 
   ░███    ░░░   ██████   ██████  █████ ████ ████████   ██████    ░███    ░░░  █████ ████  █████  ███████    ██████  █████████████      ░███   ░░███ ░███    ░███  ░███░█████░███    ░░░    ░███ ███   ░░███ ███   ░░███ ███   ░░███
   ░░█████████  ███░░███ ███░░███░░███ ░███ ░░███░░███ ███░░███   ░░█████████ ░░███ ░███  ███░░  ░░░███░    ███░░███░░███░░███░░███     ░███    ░███ ░███████████  ░███░░███ ░███       ██████░ ░███    ░███░███    ░███░███    ░███
    ░░░░░░░░███░███████ ░███ ░░░  ░███ ░███  ░███ ░░░ ░███████     ░░░░░░░░███ ░███ ░███ ░░█████   ░███    ░███████  ░███ ░███ ░███     ░███    ░███ ░███░░░░░███  ░███ ░░░  ░███      ░░░░░░███░███    ░███░███    ░███░███    ░███
    ███    ░███░███░░░  ░███  ███ ░███ ░███  ░███     ░███░░░      ███    ░███ ░███ ░███  ░░░░███  ░███ ███░███░░░   ░███ ░███ ░███     ░███    ███  ░███    ░███  ░███      ░███     ███   ░███░░███   ███ ░░███   ███ ░░███   ███ 
    ░░█████████ ░░██████ ░░██████  ░░████████ █████    ░░██████    ░░█████████  ░░███████  ██████   ░░█████ ░░██████  █████░███ █████    ██████████   █████   █████ █████     █████   ░░████████  ░░░█████░   ░░░█████░   ░░░█████░  
    ░░░░░░░░░   ░░░░░░   ░░░░░░    ░░░░░░░░ ░░░░░      ░░░░░░      ░░░░░░░░░    ░░░░░███ ░░░░░░     ░░░░░   ░░░░░░  ░░░░░ ░░░ ░░░░░    ░░░░░░░░░░   ░░░░░   ░░░░░ ░░░░░     ░░░░░     ░░░░░░░░     ░░░░░░      ░░░░░░      ░░░░░░   
                                                                                ███ ░███                                                                                                                                            
                                                                                ░░██████                                                                                                                                             
                                                                                ░░░░░░                                                                                                                                              
    """)
    params = Generator()
    hash_maker = Hasher(os.urandom(48))

    while True:
        try:
            option = json.loads(get_option())["option"]

            if option == '1':
                your_input = input(f"\nSelect the public key [0-{len(params.mods)-1}] that corresponds to your private key (json format) :: ")
                choice = int(json.loads(your_input)["choice"])
                ciphertext = params.encrypt(choice)
                response = json.dumps({'N' : params.N, 'phi' : params.phi, 'encrypted_passcode' : ciphertext})

            elif option == '2':
                your_input = input("\nWhat are we hashing today ? (json format) :: ")
                to_hash = bytes.fromhex(json.loads(your_input)["hash"])
                if len(to_hash) > 27:
                    response = {"error" : "We don't do this here..."}
                else:
                    to_hash = hash_maker.bxor(to_hash, params.rxor(to_hash))
                    digest = hash_maker.hash_digest(to_hash)
                    response = json.dumps({"hash" : digest.hex()})

            elif option == '3':
                your_input = input("\nEnter the passcode (json format) :: ")
                passcode = bytes.fromhex(json.loads(your_input)["passcode"])

                if params.passcode != passcode:
                    response = {"error" : "You need the passcode to authenticate..."}
                else:
                    your_input = input(f"\n2FA Activated: {random.choice(tfa_questions)} (json format) :: ")
                    tfa_answer = bytes.fromhex(json.loads(your_input)["answer"])
                    randomized, token = hash_maker.two_factor_generate(params.passcode, tfa_answer, params.randomize(hash_maker.hash_digest(os.urandom(64)).hex()))
                    your_input = input(f"\nOnly admins have access to all random values used to create the tokens. What is the random value of the token = {token.hex()} ? (json format) :: ")
                    authorize = bytes.fromhex(json.loads(your_input)["token"])
                    if authorize == randomized:
                        print(f"\nWell I'll be dam mate, here you go : {FLAG}")
                        exit()

            elif option == '4':
                print('bye.')
                exit()

            else:
                response = json.dumps({"error" : "Invalid Option"})
            
            print(f"\n{response}")
        except Exception as e:
            response = json.dumps({"error": str(e)})
            print(f"\n{response}\n")
            exit()

    

if __name__ == '__main__':
    main()