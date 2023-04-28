#!/usr/bin/python3

from pwn import *
import gmpy2

#context.log_level = 'debug'

#Input message as hex: 00
N = 2**1024

key = [1]*64

#print(sum(key))
ip,port = '167.99.197.168',30589
io = remote(ip,port)

while sum(key) > 32:
	io.recvuntil('>')
	io.sendline('2')
	io.recvuntil('Input message as hex:')
	io.sendline('00')  #any even number should be OK, observe the result, odd -> even is not in key

	for i in range(64):
		buf = io.recvline().strip()
		#print(buf)
		x,y = buf.decode().split(', ')
		x = int(x[1:])
		y = int(y[:-1])
		if x%2 == 0 and y%2 != 0:
			key[i] = 0

print(key)
io.recvuntil('>')
io.sendline('1')

flag = [[]]
for i in range(64):
	buf = io.recvline().strip()
	#print(buf)
	if key[i]:
		x,y = buf.decode().split(', ')
		x = int(x[1:])
		y = int(y[:-1])
		flag.append([x,y])
