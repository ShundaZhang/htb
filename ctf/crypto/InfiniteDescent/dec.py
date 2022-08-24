from Crypto.Util import number
from Crypto.PublicKey.RSA import construct
from Crypto.PublicKey import RSA
import sympy
import gmpy2

'''
def getPQ():
	n_length =512 #generates a 1024 bit key.
	while True:
		firstprime = number.getPrime(n_length) #let's get our first number
		lowerp = firstprime - 10
		upperp = firstprime + 10	   
		for x in range(lowerp,upperp): #getPrime takes too long so we'll find a nearby prime for q
			if x == firstprime:
				continue
			else:   
				if sympy.isprime(x):
					secondprime = x
					return firstprime, secondprime
					break
		return 1, 1


while True:
	p, q = getPQ()
	if p == 1:
		print("still trying")
	else:
		break

print p,q

openssl rsa -pubin -in pub.pem -text -noout
RSA Public-Key: (1023 bit)
Modulus:
	56:c3:93:ec:d8:cb:5b:5b:8f:03:e9:b1:35:9b:62:
	32:1f:06:d6:64:c1:a9:40:45:b2:71:2e:0e:90:87:
	26:a5:b0:69:c1:c7:4e:b8:54:52:07:f5:72:0a:cc:
	f2:bf:0e:dd:51:cc:c3:ba:f2:0c:bb:cc:b3:a2:ca:
	2a:4f:b5:86:f6:9f:43:3a:59:c7:43:1a:0c:3d:27:
	df:b1:c7:81:e3:5d:90:87:c7:88:78:cd:08:5f:41:
	e3:98:ca:67:92:3d:ec:17:24:e7:be:19:3d:f5:ca:
	6c:fa:fd:0d:54:97:2a:bf:8d:69:c3:5d:9a:20:c5:
	f6:d7:8b:a6:c8:c2:e3:7b
Exponent: 65537 (0x10001)

'''

n = 0x56c393ecd8cb5b5b8f03e9b1359b62321f06d664c1a94045b2712e0e908726a5b069c1c74eb8545207f5720accf2bf0edd51ccc3baf20cbbccb3a2ca2a4fb586f69f433a59c7431a0c3d27dfb1c781e35d9087c78878cd085f41e398ca67923dec1724e7be193df5ca6cfafd0d54972abf8d69c35d9a20c5f6d78ba6c8c2e37b

x = gmpy2.iroot(n, 2)[0]

'''
for i in range(x-20, x+20, 1):
	if sympy.isprime(i):
		for j in range(i-10, i+10, 1):
			if sympy.isprime(j) and i*j == n:
				print i,j
				break
'''

p = 7805622068551395034983074294227914827932592556281432557101799867160043121996329164791493852142033952331091204125384233936237118904494182099698709037828129 
q = 7805622068551395034983074294227914827932592556281432557101799867160043121996329164791493852142033952331091204125384233936237118904494182099698709037828123

c = 41296290787170212566581926747559000694979534392034439796933335542554551981322424774631715454669002723657175134418412556653226439790475349107756702973735895193117931356004359775501074138668004417061809481535231402802835349794859992556874148430578703014721700812262863679987426564893631600671862958451813895661

phi = (p-1)*(q-1)
e = 65537
d = gmpy2.invert(e, phi)

m = pow(c, d, n)
print m
#!/usr/bin/env python
#**********************************************************************
# filename: AESbootstrap.py
# version: 0.11.7-alpha
# release date: 20170801
# dev: Cayce Pollard
# qa: Jonathan Norrell
# instantiate mersenne each time, feed it every 3 digits of the shared secret
# to establish a shared AES128 key.
#
#**********************************************************************

#textbook mersenne twister from https://en.wikipedia.org/wiki/Mersenne_Twister#Python_implementation (no rolling your own!)

class mersenne(object):

	def __init__(self, seed):
		# Initialize the index to 0
		self.index = 624
		self.mt = [0] * 624
		self.mt[0] = seed  # Initialize the initial state to the seed
		for i in range(1, 624):
			initval = int(0xFFFFFFFF & (1812433253 * (self.mt[i - 1] ^ self.mt[i - 1] >> 30) + i))
			# print(initval)
			self.mt[i] = initval


	def extract_number(self):
		if self.index >= 624:
			self.twist()

		y = self.mt[self.index]

		# Right shift by 11 bits
		y = y ^ y >> 11
		# Shift y left by 7 and take the bitwise and of 2636928640
		y = y ^ y << 7 & 2636928640
		# Shift y left by 15 and take the bitwise and of y and 4022730752
		y = y ^ y << 15 & 4022730752
		# Right shift by 18 bits
		y = y ^ y >> 18

		self.index = self.index + 1

		return int(0xFFFFFFFF & y)

	def twist(self):
		for i in range(624):
			# Get the most significant bit and add it to the less significant
			# bits of the next number
			y = int(0xFFFFFFFF & ((self.mt[i] & 0x80000000) + (self.mt[(i + 1) % 624] & 0x7fffffff)))
			self.mt[i] = self.mt[(i + 397) % 624] ^ y >> 1

			if y % 2 != 0:
				self.mt[i] = self.mt[i] ^ 0x9908b0df
		self.index = 0
		#test


#******************************************************************************
#test tool:
#use this to convert a triplet from the decoded value as seedval
#do this across each of the values to check the candidate against the AESkey.
#******************************************************************************
def gen_and_check(genseed):
	# make an object
	x = mersenne(genseed)
	y = (x.extract_number() & 0xFF) #only interested in LSBs. Use the mask as we don't care about the rest

	return y #candidate for comparison.

#instantiate mersenne each time, feed it every 3 digits of the shared secret!!!
#triplet!!!!
#500491164140527509149577108534901274218266116126419727365281831678182316
m = [500,491,164,140,527,509,149,577,108,534,901,274,218,266,116,126,419,727,365,281,831,678,182,316]
fb = ''
for x in m:
	list = str(bin(gen_and_check(x)))
	candidate = list[2::]
	candidate = candidate.zfill(8)
	fb += candidate

flag = ''
for i in range(0, len(fb), 8):
	flag += chr(int(fb[i:i+8],2))

print flag
#base64
#ZmxhZz1Ccm9rM25fRzRtZQ==
#flag=Brok3n_G4me
#HTB{Brok3n_G4me}
