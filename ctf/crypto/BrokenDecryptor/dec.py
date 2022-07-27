from pwn import *

#HTB{XXXXXXXXXX}
#15 bytes
#From the source code, no 00 to xor, so the orginal value is the one which never hit by xor...

flag = ''
#ip,port = '127.0.0.1',1337
ip,port = '68.183.36.105',31728
io = remote(ip, port)

io.recvuntil('Your option:')

f = []
for _ in range(15):
	f.append([True for x in range(256)])

for _ in range(2400):
	print _
	io.sendline('1')
	px = io.recvuntil('Your option:').split('\n')[0].lstrip()
	for j in range(15):
		f[j][int(px[2*j:2*j+2],16)] = False

enc = ''
for i in range(15):
	for j in range(256):
		if f[i][j] == True:
			enc += hex(j)[2:].zfill(2)
print enc

f = []
for _ in range(15):
	f.append([True for x in range(256)])

for _ in range(2400):
	print _
	io.sendline('2')
	io.recvuntil('Enter plaintext: ')
	io.sendline(enc)
	px = io.recvuntil('Your option:').split('\n')[0].lstrip()
	for j in range(15):
		f[j][int(px[2*j:2*j+2],16)] = False

for i in range(15):
	for j in range(256):
		if f[i][j] == True:
			print chr(j)
			flag += chr(j)

print flag
#HTB{1V_r3u$3#!}
