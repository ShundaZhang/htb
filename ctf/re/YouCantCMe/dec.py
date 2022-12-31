from pwn import *

f = p64(0x5517696626265e6d)+p64(0x555a275a556b266f)+p32(0x29635559)
flag = ''
for i in f:
	flag += chr(ord(i)+ord('\n'))

print flag
