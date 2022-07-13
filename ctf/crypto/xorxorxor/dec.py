from pwn import *
enc = '134af6e1297bc4a96f6a87fe046684e8047084ee046d84c5282dd7ef292dc9'.decode('hex')
for i in range(len(enc)):
	print xor(xor(enc[i:i+4],'HTB{'),enc)
