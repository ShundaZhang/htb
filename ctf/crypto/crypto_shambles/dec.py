from pwn import *

def bitflip(buf,index,padding,c1,io):
	for i in range(256):
		b = hex(i)[2:].zfill(2)
		x = buf[:32-2*index]+b+padding+c1
		io.sendline('1')
		io.recvuntil('Send your credentials:')
		x = '{"token":"'+x+'"}'
		io.sendline(x)
		rbuf = io.recvuntil('>')
		if not b'Decryption error!' in rbuf:
			print('=================================')
			print('index: ',index)
			print('Hit!: ', b)
			print('keybits: ', hex(i^index)[2:].zfill(2))
			return hex(i^index)[2:].zfill(2)

ip, port = '94.237.60.154', 54168
io = remote(ip, port)

io.recvuntil('>')

io.sendline('1')

io.recvuntil('Send your credentials:')

io.sendline('{"token":"","username":"D-Cryp7","password":"Cryp70Gr47Hy!"}')

bufx = io.recvuntil('>')
bufx = bufx.decode().split('\n')[0].split(': ')[1]

print(bufx)
print(len(bufx))

io.sendline('2')
buf = io.recvuntil('>')
buf = buf.decode().split('\n')[0].split(': ')[1]

print(buf)
print(len(buf))


'''
iv = buf[:32]
c1 = buf[32:]

padding = ''
keystream = ''
buf0 = '0'*32
for index in range(1,17,1):
	keyx = bitflip(buf0, index, padding, c1, io)
	keystream = keyx + keystream
	padding = ''
	for j in range(index):
		padding += hex(int(keystream[2*j:2*j+2],16)^(index+1))[2:].zfill(2)
	print('-----------------------------------')
	print('keystream: ',keystream)
	print('padding: ',padding)

print(xor(bytes.fromhex(keystream),bytes.fromhex(iv)))

print('**************************************')
print(iv)
print(keystream)

#1337.0
'''

'''
flag = ''
for i in range(16):
	flag += chr(int(keystream[2*i:2*i+2],16)^int(iv[2*i:2*i+2],16))
print(flag)
'''

'''
iv = 'ff'*16
c1 = bufx[:32]

padding = ''
keystream = ''
buf0 = '0'*32
for index in range(1,17,1):
	keyx = bitflip(buf0, index, padding, c1, io)
	keystream = keyx + keystream
	padding = ''
	for j in range(index):
		padding += hex(int(keystream[2*j:2*j+2],16)^(index+1))[2:].zfill(2)
	print('-----------------------------------')
	print('keystream: ',keystream)
	print('padding: ',padding)


#print(xor(bytes.fromhex(keystream),bytes.fromhex(iv)))

print('**************************************')
print(iv)
print(keystream)
ks = bytes.fromhex(keystream)

import json, os, time, jwt, datetime
payload = {
	"username": "D-Cryp7",
	"exp": datetime.datetime.utcnow() + datetime.timedelta(days = 1)
}
JWT_SECRET = os.urandom(32)
token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
pt = token[:16]

#From jwt.io, typ and alg orders are differnet!
pt = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'[:16]
IV = xor(pt, ks)

iv = 'ff'*16
c1 = buf[:32]

padding = ''
keystream = ''
buf0 = '0'*32
for index in range(1,17,1):
	keyx = bitflip(buf0, index, padding, c1, io)
	keystream = keyx + keystream
	padding = ''
	for j in range(index):
		padding += hex(int(keystream[2*j:2*j+2],16)^(index+1))[2:].zfill(2)
	print('-----------------------------------')
	print('keystream: ',keystream)
	print('padding: ',padding)

#print(xor(bytes.fromhex(keystream),bytes.fromhex(iv)))

print('**************************************')
print(iv)
print(keystream)
ks1 = bytes.fromhex(keystream)

pt1 = xor(IV,ks1)
print(pt1)
'''

pt1 = '4153217235184108'
io.sendline('3')
io.recvuntil('Insert your card number:')
io.sendline(pt1)
io.recvuntil('Quantity:')
io.sendline('1337')

print(io.recvline())
print(io.recvline())
print(io.recvline())

#HTB{Sw4pp1nG_Bl0cK5_m4K35_7h15_P4dd1nG_0R4Cl3_S7uff_70_W0rK!}
