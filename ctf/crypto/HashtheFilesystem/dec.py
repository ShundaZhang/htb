#!/usr/bin/env python3.9
from pwn import *
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Util.number import bytes_to_long
from Crypto.Util.Padding import pad, unpad
import signal
import socketserver
import time
import os
import json

file_record = {}


def initializeDatabase():
	fnames = []
	directory = "./uploads/"
	for file in os.listdir(directory):
		file = directory + file
		with open(file, "rb") as f:
			data = f.read()
			fname = uploadFile(data, os.urandom(100))
		os.rename(file, directory + fname)
		fnames.append(fname)
	return fnames


def encrypt(key, msg):
	iv = os.urandom(16)
	ctr = Counter.new(128, initial_value=bytes_to_long(iv))
	cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
	padded = pad(msg, 16)
	return iv, cipher.encrypt(padded).hex()


def decrypt(key, iv, ct):
	ctr = Counter.new(128, initial_value=bytes_to_long(iv))
	cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
	return unpad(cipher.decrypt(ct), 16)

def getFname(passphrase):
	tphrase = tuple(passphrase)
	return hex(hash(tphrase)).replace('0x', '').replace('-', 'ff')


def uploadFile(dt, passphrase):
	fname = getFname(passphrase)
	open('./uploads/' + fname, 'wb').write(dt)
	return fname


def readFile(fname):
	return open('./uploads/' + fname, 'rb').read()


def challenge(req):
	fnames = initializeDatabase()
	file_record['admin'] = [fname for fname in fnames]

	req.sendall(b'Super secret file server for malicious operations.\n' +
				b'Who are you:\n' + b'> ')
	user = req.recv(4096).decode().strip()

	if user == 'admin':
		req.sendall(
			b'Administrator can access the server only via ssh.\nGoodbye!\n')
		return

	token = json.dumps({'username': user, 'timestamp': str(time.time())})
	file_record[user] = []

	key = os.urandom(16)
	iv, token_ct = encrypt(key, token.encode())

	req.sendall(b'Your token is: ' + token_ct.encode() + b'\n')
	while True:
		req.sendall(
			b'1. Upload a file.\n2. Available files.\n3. Download a file.\n')
		req.sendall(b'> ')
		option = req.recv(4096).decode().strip()

		try:
			if option == '1':
				req.sendall(b'Submit your token, passphrase, and file.\n')
				res = json.loads(req.recv(4096).decode().strip())

				token_ct = bytes.fromhex(res['token'])
				token = json.loads(decrypt(key, iv, token_ct))
				if token['username'] not in file_record.keys():
					file_record[token['username']] = []

				dt = bytes.fromhex(res['data'])
				passphrase = res['passphrase']
				fname = uploadFile(dt, passphrase)
				file_record[token['username']].append(fname)

				payload = json.dumps({'success': True})
				req.sendall(payload.encode() + b'\n')

			elif option == '2':

				req.sendall(b'Submit your token.\n')
				res = json.loads(req.recv(4096).decode().strip())

				token_ct = bytes.fromhex(res['token'])
				token = json.loads(decrypt(key, iv, token_ct))

				if token['username'] not in file_record.keys():
					payload = json.dumps({'files': []})
				else:
					files = file_record[token['username']]
					payload = json.dumps({'files': files})

				req.sendall(payload.encode() + b'\n')

			elif option == '3':
				req.sendall(b'Submit your token and passphrase.\n')
				res = json.loads(req.recv(4096).decode().strip())

				token_ct = bytes.fromhex(res['token'])
				token = json.loads(decrypt(key, iv, token_ct))

				passphrase = res['passphrase']
				fname = getFname(passphrase)
				files = file_record[token['username']]

				if fname not in files:
					payload = json.dumps({'filename': fname, 'success': False})
				else:
					content = readFile(fname).hex()
					payload = json.dumps({
						'filename': fname,
						'success': True,
						'content': content
					})

				req.sendall(payload.encode() + b'\n')

			else:
				req.sendall(b'Wrong option.')
		except:
			req.sendall(b'An error has occured. Please try again.\n')


class incoming(socketserver.BaseRequestHandler):

	def handle(self):
		signal.alarm(30)
		req = self.request
		challenge(req)


class ReusableTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
	pass


def main():
	socketserver.TCPServer.allow_reuse_address = True
	server = ReusableTCPServer(("0.0.0.0", 1337), incoming)
	server.serve_forever()

ip, port = "134.209.186.13", 32656

if __name__ == "__main__":
	'''
	#For test
	user = 'admim'	
	token = json.dumps({'username': user, 'timestamp': str(time.time())})
	print(token.encode())
	key = os.urandom(16)
	iv, token_ct = encrypt(key, token.encode())
	print(token_ct)
	#token_ct = bytes.fromhex(token_ct)
	#token_pt = decrypt(key, iv, token_ct)
	#print(token_pt)
	print(chr(token.encode()[18]))
	x = xor(chr(token.encode()[18]), chr(bytes.fromhex(token_ct)[18]), 'n')
	print(x.decode())
	token_ct2 = bytes.fromhex(token_ct)[:18]+x+bytes.fromhex(token_ct)[19:]
	print(token_ct2.hex())
	token_pt = decrypt(key, iv, token_ct2)
	print(token_pt)
	'''

	p = remote(ip, port)
	p.recvuntil(">")
	p.sendline("admim")
	p.recvuntil("Your token is:")
	token_ct = p.recvline().split()[3]
	x = xor('m', chr(bytes.fromhex(token_ct)[18]), 'n')
	token_ct2 = bytes.fromhex(token_ct)[:18]+x+bytes.fromhex(token_ct)[19:]
	print(token_ct2.hex())
	
	p.recvuntil(">")
	p.sendline("2")
	p.recvuntil("Submit your token.")
	token = '{"token": '+token_ct2.hex()+'}'
	p.sendline(token)
	print(p.recvline())
	print(p.recvline())
	print(p.recvline())
	print(p.recvline())
	print(p.recvline())
	print(p.recvline())
	print(p.recvline())
	
