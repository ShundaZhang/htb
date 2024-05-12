from re import search as rsearch
from base64 import b64encode, b64decode
from hashlib import sha256
from sympy.ntheory import factorint as ps_and_qs
from Crypto.PublicKey import RSA
from Crypto.Util.number import getPrime, bytes_to_long
from secret import FLAG

def show_menu():
    return input("""
An improved signing server with extra security features such as hashing usernames to avoid forging tokens!
Available options:

[0] Register an account.
[1] Login to your account.
[2] PublicKey of current session.
[3] Exit.

[+] Option >> """)

class Signer:
    def __init__(self, key_size=2048):
        self.key_size = key_size
        self.admin = bytes_to_long(b'System_Administrator')
        self.golden_ratio = 2654435761
        self.hash_var = lambda key: (((key % self.golden_ratio) * self.golden_ratio) >> 32)
        self.equation_output = lambda k, rnd: (k * rnd) % self.golden_ratio

        rsa_key = RSA.generate(key_size)
        self.n = rsa_key.n
        self.d = rsa_key.d
        self.e = rsa_key.e

    def numgen(self):
        while True:
            rnd = getPrime(32)
            if rnd < self.golden_ratio:
                return rnd

    def sign(self, username):
        h = self.hash_var(username)
        auth = pow(int(h), self.d, self.n)
        return auth

    def verify(self, recomputed_signature, token):
        return recomputed_signature == pow(token, self.e, self.n)

    def equations(self):
        h_n = self.hash_var(self.n)
        ps_n_qs = [k**v for k, v in ps_and_qs(h_n).items()]
        rnds = [self.numgen() for _ in ps_n_qs]
        return [f"equation(unknown, {rnd}, {self.golden_ratio}) = {self.equation_output(unknown, rnd)}" for unknown, rnd in zip(ps_n_qs, rnds)]

def main():
    signer = Signer()
    
    while True:
        user_inp = show_menu()
        if user_inp == '0':
            username = input("Enter a username: ")
            if rsearch('[^a-zA-Z0-9]', username):
                print("[-] Invalid characters detected. Symbols are not allowed.")
                continue

            numeric_username = int(username.encode().hex(), 16)

            if numeric_username % signer.golden_ratio == signer.admin % signer.golden_ratio:
                print("[-] Admin user already exists.")
                continue

            token = signer.sign(numeric_username)
            print(f"Your session token is {b64encode(str(token).encode())}")

        elif user_inp == '1':
            username = input("Enter your username: ")
            authToken = input("Enter your authentication token: ")

            try:
                authToken = b64decode(authToken.encode())
                authToken = int(authToken.decode())
            except:
                print("[-] Invalid format for authentication key.")
                continue
            
            numeric_username = int(username.encode().hex(), 16)

            recomputed_signature = signer.hash_var(numeric_username)
            if signer.verify(recomputed_signature, authToken):
                if numeric_username == signer.admin:
                    print(f"[+] Welcome back admin! The note you left behind from your previous session was: {FLAG}")
                else:
                    print(f"[+] Welcome {username}!")
            else:
                print("[-] No match found for that (username, token) pair.")

        elif user_inp == '2':
            print(f"\nTo avoid disclosing public keys to bots, a modern captcha must be completed. Kindly compute the hash of 'N' to get the full public key based on the following equations:\n{signer.equations()}\n")
            
            try:
                user_result = int(input("Enter the hash(N): "))
            except:
                print("Invalid input for a hash.")
                continue

            if user_result == signer.hash_var(signer.n):
                print(f"[+] Captcha successful!\n(e,N) = {(signer.e, signer.n)}")

        elif user_inp == '3':
            print("[-] Closing connection.")
            break

        else:
            print("[-] Invalid selection.")

if __name__ == '__main__':
    main()
