import json
import signal
import subprocess
import socketserver

from hashlib import sha1
from random import randint
from Crypto.Util.number import bytes_to_long, long_to_bytes


FLAG = 'HTB{dummyflag}'
class ECDSA:
	def __init__(self):
		self.n = 115792089210356248762697446949407573529996955224135760342422259061068512044369
		self.k = 0
		self.g = 5
		self.key = ... #choose your own key

	def sign(self, pt):
		h = sha1(pt).digest()
		h = bytes_to_long(h)
		h = bin(h)[2:]
		h = int(h[:len(bin(self.n)[2:])], 2)
		self.k = randint(1, self.n-1)
		r = pow(self.g, self.k, self.n)
		s = (pow(self.k, -1, self.n) * (h + self.key * r)) % self.n
		lsb = self.k % (2 ** 7)
		return {"h": hex(h)[2:], "r": hex(r)[2:], "s": hex(s)[2:], "lsb": bin(lsb)[2:] }

	def verify(self, pt, sig_r, sig_s):

		h = sha1(pt).digest()
		h = bytes_to_long(h)
		h = bin(h)[2:]
		h = int(h[:len(bin(self.n)[2:])], 2)
		sig_r = int(sig_r, 16)
		sig_s = int(sig_s, 16)
		
		c = pow(sig_s, -1, self.n)
		k = (c *(h +self.key*sig_r)) %self.n
		
		if sig_r== pow(self.g,k,self.n ):
			if pt ==b'william;yarmouth;22-11-2021;09:00':
				return 'Your appointment has been confirmed, congratulations!\n' +\
						'Here is your flag: ' + FLAG
			else:
				return 'Your appointment has been confirmed!\n'
		else: return 'Signature is not valid\n'


def challenge(req):
	cipher = ECDSA()
	
	req.sendall(b'Welcome to the SteamShake transplant clinic where our mission is to deliver the most vintage and high tech arms worldwide.\n'+\
					b'Please use your signature to verify and confirm your appointment.\nEstimated waiting for next appointment: 14 months\n> ')
	try:
			
		dt = json.loads(req.recv(4096).strip())

		res = cipher.verify(dt['pt'].encode(), dt['r'], dt['s'])
		req.sendall(res.encode())
	except Exception as e:
		req.sendall(b'Invalid payload.\n')
		exit(1)
	
	

class incoming(socketserver.BaseRequestHandler):
	def handle(self):
		signal.alarm(300)
		req = self.request
		challenge(req)

class ReusableTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
	pass


def main():
	socketserver.TCPServer.allow_reuse_address = True
	server = ReusableTCPServer(("0.0.0.0", 2310), incoming)
	server.serve_forever()

if __name__ == "__main__":
	main()
