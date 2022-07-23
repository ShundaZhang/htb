from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes, isPrime

e = getPrime(128)
while True:
  p, q = getPrime(512), getPrime(512)
  if (p-1) % e and (q-1) % e:
    break

n = p * q
d = pow(e,-1,(p-1)*(q-1))

pubkey = (n, e)
privkey = (n, d)

def sign(message, privkey):
    n, d = privkey
    return pow(message, d, n)
    
def verify(message, signature, pubkey):
    n, e = pubkey
    if pow(signature, e, n) == message:
        return True
    else:
        return False

to_sign = bytes_to_long(b"Username: Admin, Access code: CryptoBestCategoryF3")
assert isPrime(to_sign)

menu = """
[1] Sign a message
[2] Verify access to this server
[3] Exit
"""[1:]

print("Welcome to your Signing Server. With our verifying feature, we don't even need to give you our public key!")
while True:
  print(menu)
  try:
    opt = input("Enter your option: ")
    if opt == "1":
      msg = int(input("Enter your message to be signed as a decimal integer: "))
      if msg % n == to_sign:
        print("You cannot sign the admin message.")
      else:
        print(f"Signature for {msg}: {sign(msg, privkey)}")
    elif opt == "2":
      msg = int(input("Enter your message as a decimal integer: ")) % n
      sig = int(input("Enter your signature as a decimal integer: ")) % n
      if verify(msg, sig, pubkey):
        if msg == to_sign:
          print(f"Welcome, admin. Here's your flag: {open('/challenge/flag.txt').read().strip()}")
        else:
          print("Signature valid!")
      else:
        print("Signature invalid.")
    elif opt == "3":
      print("Goodbye.")
      exit(0)
    else:
      print("Option not recognized, please try again.")
  except Exception as error:
    print("An error occured, please try again.", error)
