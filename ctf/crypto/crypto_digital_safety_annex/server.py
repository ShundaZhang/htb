import random
import binascii
from base64 import b64encode, b64decode
from hashlib import sha256
from Crypto.PublicKey import DSA as PrimeGenerator
from secret import FLAG, HTB_PASSWD

def show_menu():
    return input("""
Welcome to the Digital Safety Annex!
We will keep your data safe so you don't have to worry!

[0] Create Account 
[1] Store Secret
[2] Verify Secret
[3] Download Secret
[4] Developer Note
[5] Exit

[+] Option > """)

class DSA:
    def __init__(self, key_size=2048):
        key = PrimeGenerator.generate(key_size)
        self.p, self.q = key.p, key.q
        self.x, self.y, self.g = self.generate_keys()
        self.k_min = 65500

    def get_public_params(self):
        return (self.p, self.q, self.g)

    def generate_keys(self):
        h = random.randint(2, self.p-2)
        g = pow(h, (self.p-1)//self.q, self.p)
        x = random.randint(1, self.q-1)
        y = pow(g, x, self.p)
        return x, y, g

    def sign(self, h, k_max):
        k = random.randint(self.k_min, k_max)
        r = pow(self.g, k, self.p) % self.q
        s = (pow(k, -1, self.q) * (int(h, 16) + self.x * r)) % self.q
        return (r, s)

    def verify(self, h, signature):
        r, s = signature
        r = int(r)
        s = int(s)
        w = pow(s, -1, self.q)
        u1 = (int(h, 16) * w) % self.q
        u2 = (r * w) % self.q
        v = ((pow(self.g, u1, self.p) * pow(self.y, u2, self.p)) % self.p) % self.q
        return r == v

class Account:
    def __init__(self, username="default-user", passwd=""):
        self.username = username
        self.password = sha256(passwd.encode()).digest()
        self.k_max = int(len(self.username) ** 6)
        if self.k_max < 65536:
            self.k_max += 1000000
        self.stored_msgs = 0

    def login(self, pw=""):
        if pw == "":
            pw = input("Enter your password : ")
        return sha256(pw.encode()).hexdigest() == self.password.hex()

class Annex:
    def __init__(self):
        self.user_log = []
        self.users = {}
        self.vault = {}
        self.dsa = DSA()

    def create_account(self, username="", password=""):
        if (username == "" and password == ""):
            print("\n[+] Thank you for choosing the Digital Safety Annex!")
            username = input("\n[+] To get started, please enter your username: ")
            if username in self.users.keys():
                print("\n[!] Username already exists!")
                return
            password = input("[+] Next, enter your password: ")
        account = Account(username, password)
        self.users[username] = account
        return username

    def log_info(self, account, msg, h, sig):
        _id = account.stored_msgs
        if account.username not in self.vault.keys():
            self.vault[account.username] = []
        
        self.vault[account.username].append((h, msg, (str(sig[0]), str(sig[1]))))
        self.user_log.append((sig, h))
        account.stored_msgs += 1

    def sign(self, username, message, password=""):
        account = self.users[username]
        
        if (account.login(password) == False):
            print("[!] Invalid Password!\n")
            return (-1, -1)

        msg = message.encode()
        h = sha256(msg).hexdigest()
        
        r, s = self.dsa.sign(h, account.k_max)
        
        self.log_info(account, msg, h, (r, s))
        
        return (r, s)

    def verify(self, message, signature):
        msg = message.encode()
        h = sha256(msg).hexdigest()
        return self.dsa.verify(h, signature)

    def download(self, priv, nonce, req_id, username):
        if username not in self.vault.keys():
            print(f"[!] Could not find any submissions of user {username} in the vault!")
            return

        if len(self.vault[username]) < req_id:
            print(f"[!] Something went wrong with accessing request id!")
            return 

        h, m, sig = self.vault[username][req_id]
        
        p, q, g = self.dsa.get_public_params()
 
        rp = pow(g, nonce, p) % q
        sp = (pow(nonce, -1, q) * (int(h, 16) + priv * rp)) % q

        new_sig = (str(rp), str(sp))

        if new_sig == sig:
            print(f"[+] Here is your super secret message: {m}")
        else:
            print(f"[!] Invalid private key or nonce value! This attempt has been recorded!")

def main():
    annex = Annex()
    annex.create_account("Admin", "5up3r_53cur3_P45sw0r6")
    annex.create_account("ElGamalSux", HTB_PASSWD)
    annex.sign("ElGamalSux", "DSA is a way better algorithm", HTB_PASSWD)
    annex.sign("Admin", "Testing signing feature", "5up3r_53cur3_P45sw0r6")
    annex.sign("ElGamalSux", "I doubt anyone could beat it", HTB_PASSWD)
    annex.sign("Admin", "I should display the user log and make sure its working", "5up3r_53cur3_P45sw0r6")
    annex.sign("ElGamalSux", "To prove it, I'm going to upload my most precious item! No one but me will be able to get it!", HTB_PASSWD)
    annex.sign("ElGamalSux", FLAG, HTB_PASSWD)

    account_username = ""

    while True:
        user_inp = show_menu()
        
        if user_inp == '0':
            account_username = annex.create_account()
        
        elif user_inp == '1':
            if not account_username:
                print("\n[!] You need to create an account with the Annex first before you can store any secrets!")
            
            else:
                message = input("\nPlease enter you super secret message : ")
                r, s = annex.sign(account_username, message)

                if r == -1 and s == -1:
                    continue

                print(f"\n[+] Here is your signature (r,s): ({r}, {s})")
                print("Keep your signature safe!!")
        
        elif user_inp == '2':
            signature = input("\nPlease enter the signature (r,s) separated by a comma: ")
            signature = signature.replace(" ", "").split(',')
            if len(signature) < 2 or not signature[0].isdigit() or not signature[1].isdigit():
                print("\n[!] Sorry, need a valid signature to verify message!")
                continue

            message = input("\nPlease enter the message you wish to verify : ")
            if not message or message == " ":
                print("\n[!] Sorry, need a valid message to continue verification!")
                continue

            if annex.verify(message, signature):
                print("[+] Message has been successfully verified!")
            else:
                print("[!] Message could not be verified! Please make sure your signature and messages are correct!")

        elif user_inp == '3':
            uname = input("\nPlease enter the username who stored the message : ")
            if not uname or uname == " ":
                print("\n[!] Sorry, need valid username to download secret!")
                continue
            
            req_id = input("\nPlease enter the message's request id: ")
            if not req_id or req_id == " " or not req_id.isdigit():
                print("\n[!] Sorry, need valid request id to download secret!")
                continue

            if uname == account_username:
                account = annex.users[account_username]
                if account.login():
                    _, _, msg, _ = annex.vault[uname][int(req_id)]
                    print(f"\n[+] Here is your message: {msg}")
            else:
                k = input("\nPlease enter the message's nonce value : ")
                if not k or k == " " or not k.isdigit():
                    print("\n[!] Sorry, need a valid signature to download secret!")
                    continue
            
                x = input("\n[+] Please enter the private key: ")
                if not x or x == " " or not x.isdigit():
                    print("\n[!] Sorry, need a valid signature to download secret!")
                    continue

                annex.download(int(x), int(k), int(req_id), uname)
        
        elif user_inp == '4':
            print("\nWe are here to prove that DSA is waaayyyy better than El Gamal! \nWe also modified our signature algorithm to use the super secure SHA-256. No way you can bypass our authentication. If you must try, be sure to bring tissues for your tears of failure.\nI'll throw you a bone, these are public record anyway:\n")

            p, q, g = annex.dsa.get_public_params()

            print(f"\np = {p}\nq = {q}\ng = {g}\n")

            inp = input("[+] Test user log (y/n) : ")
            if (inp == 'y'):
                if annex.users['Admin'].login():
                    print(f'\n{annex.user_log}')
        
        elif user_inp == '5':
            print("[!] Leaving the Annex. Thanks for choosing DSA!")
            break
        
        else:
            print("[!] Invalid Selection.")


if __name__ == "__main__":
    main()
