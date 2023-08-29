from pwn import *

#context.log_level = 'debug'

ip, port = '157.245.43.189', 31152
io = remote(ip, port)

padding = 'CryptoHackTheBox'
padding_set = '}CryptoHackTheBx'

s_char = '\xdf'

for c in padding_set:
	pt = c + padding[:-1] + 'A'*15+s_char
	io.recvuntil('Message for encryption:')
	io.sendline(pt.encode())
	ct = io.recvline()[1:-1]
	if ct[:32] == ct[-32*2:-32*1]:
		print("Ending char: "+c)
		break

compare_set = 'CryptoHackTCryp'
index = 2
offset = 12
flag = ''

for i in range(4*16+5):
	if (i - 5)%16 == 0:
		index += 1
		offset = 1
	for x in range(0x20,0x7f,1):
		c = chr(x)
		pt = c + compare_set + 'A'*(16-offset) + s_char*offset
		io.recvuntil('Message for encryption:')
		io.sendline(pt.encode())
		ct = io.recvline()[1:-1]
		if ct[:32] == ct[-32*index:-32*(index-1)]:
			flag = c + flag
			compare_set = c + compare_set[:-1]
			break

print(flag)

