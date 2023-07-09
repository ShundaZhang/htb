#!/usr/bin/python3

from hashlib import sha256
from pwn import *

#context.log_level = 'debug'

ip, port = sys.argv[1].split(':')
io = remote(ip, int(port))

c = chr(0)
i = 1
flag = ''

while c != '}':
	io.recvuntil('>')
	io.sendline(b'1')
	io.recvuntil('Enter your message: ')
	io.sendline(b'\x00'*i)
	_hash = io.recvline().decode().strip().split(' ')[1]

	for ci in range(0x20,0x7f,1):
		c = chr(ci)
		f = flag + c

		if sha256(f.encode()).digest().hex() == _hash:
			break
	flag += c
	print(flag)
	i += 1

#HTB{r0ll1n6_0v3r_x0r_w17h_h@5h1n6_0r@cl3_15_n07_s3cur3!@#}
