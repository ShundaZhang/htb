from pwn import *

context.log_level = 'debug'

ip, port = '157.245.43.189', 31152
io = remote(ip, port)

padding = 'CryptoHackTheBox'
padding_set = '}CryptoHackTheBx'

s_char = '\xdf'

for c in padding_set:
	pt = c + padding[:-1] + 'A'*15+s_char
	io.recvuntil('Message for encryption:')
	io.sendline(pt)
	io.recvline()
	ct = io.recvline()[1:-1]
	print(ct)
	#if ct[:32] == ct[-32*3:-32*2]:
	#	print("Ending char: "+c)
	#	break
	
