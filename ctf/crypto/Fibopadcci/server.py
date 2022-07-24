import socketserver
from Crypto.Cipher import AES
import os
#from secret import flag, key
key = 'abcdefghijklmnop'
flag = 'HTB{7357_f149}'


fib = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 121, 98, 219, 61]

wlc_msg = """
-------------------------------------------------------------------------
|           Welcome to my Super Secure Encryption service!              |
|        We use AES along with custom padding for authentication        |
|         for extra security, so only admins should be able to          |
|          decrypt the flag with the key I have provided them!          |
|       Admins: Feel free to send me messages that you have             |
|       encrypted with my key, but make sure they are padded            |
|       correctly with my custom padding I showed you (fibopadcci)      |
|          Also, please use the a value I gave you last time,           |
|   if you need it, ask a fellow admin, I don't want some random        |
|               outsiders decrypting our secret flag.                   |
-------------------------------------------------------------------------
"""[1:]

menu_msg = """\n
-------------------------
| Menu                  |
-------------------------
|[0] Encrypt flag.      |
|[1] Send me a message! |
-------------------------
"""[1:]

def xor(a, b):
	return bytes([_a ^ _b for _a, _b in zip(a, b)])


def pad(data): #Custom padding, should be fine!
	c = 0
	while len(data) % 16:
		pad = str(hex(fib[c] % 255))[2:]
		data += unhex("0" * (2-len(pad)) + pad)
		c += 1
	return data


def checkpad(data):
	
	if len(data) % 16 != 0:
		return 0
	char = data[-1]

	try:
		start = fib.index(char)
	except ValueError:

		return 0
	
	newfib = fib[:start][::-1]

	for i in range(len(newfib)):
		char = data[-(i+2)]
		if char != newfib[i]:
			return 0
	return 1

def unhex(data):
	return bytes.fromhex(data)

class SuperSecureEncryption: # This should be unbreakable!
	def __init__(self, key):
		self.cipher = AES.new(key, AES.MODE_ECB)

	def encrypt(self, data):
		data = pad(data)
		
		a = os.urandom(16).replace(b'\x00', b'\xff') 
		b = os.urandom(16).replace(b'\x00', b'\xff')

		lb_plain = a
		lb_cipher = b
		output = b''

		data  = [data[i:i+16] for i in range(0, len(data), 16)]

		for block in data:
	
			enc = self.cipher.encrypt(xor(lb_cipher, block))
			enc = xor(enc, lb_plain)
			output += enc
			lb_plain = block
			lb_cipher = enc
		return output, a.hex(), b.hex()

	def decrypt(self, data, a, b):
		lb_plain = a
		lb_cipher = b
		output = b''
		data = [data[i:i+16] for i in range(0, len(data), 16)]
		for block in data:
			dec = self.cipher.decrypt(xor(block, lb_plain))
			dec = xor(dec, lb_cipher)
			output += dec
			lb_plain = dec
			lb_cipher = block
		if checkpad(output):
			return output
		else:
			return None

def encryptFlag():
	encrypted, a, b = SuperSecureEncryption(key).encrypt(flag)
	return f'encrypted_flag: {encrypted.hex()}\na: {a}\nb: {b}'

def sendMessage(ct, a, b):
	if len(ct) % 16:
		return "Error: Ciphertext length must be a multiple of the block length (16)!"
	if len(a) != 16 or len(b) != 16:
		return "Error: a and b must have lengths of 16 bytes!"
	decrypted = SuperSecureEncryption(key).decrypt(ct, a, b)
	if decrypted != None:
		return "Message successfully sent!"
	else:
		return "Error: Message padding incorrect, not sent."

def handle(self):
	self.write(wlc_msg)
	while True:
		self.write(menu_msg)
		option = self.query("Your option: ")
		if option == "0":
			self.write(encryptFlag())
		elif option == "1":
			try:
				ct = unhex(self.query("Enter your ciphertext in hex: "))
				b = unhex(self.query("Enter the B used during encryption in hex: "))
				a = b'HTB{th3_s3crt_A}' # My secret A! Only admins know it, and plus, other people won't be able to work out my key anyway!
				self.write(sendMessage(ct,a,b))
			except ValueError as e:
			  self.write("Provided input is not hex!")
		else:
			self.write("Invalid input, please try again.")




class RequestHandler(socketserver.BaseRequestHandler):
	handle = handle

	def read(self, until='\n'):
		out = ''
		while not out.endswith(until):
			out += self.request.recv(1).decode()
		return out[:-len(until)]

	def query(self, string=''):
		self.write(string, newline=False)
		return self.read()

	def write(self, string, newline=True):
		self.request.sendall(str.encode(string))
		if newline:
			self.request.sendall(b'\n')

	def close(self):
		self.request.close()

class Server(socketserver.ForkingTCPServer):

	allow_reuse_address = True

	def handle_error(self, request, client_address):
		self.request.close()

port = 1337
server = Server(('0.0.0.0', port), RequestHandler)
server.serve_forever()
