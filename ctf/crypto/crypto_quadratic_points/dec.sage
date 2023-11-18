from pwn import *

ip, port = '206.189.24.162',32136
io = remote(ip, port)


for _ in range(10):
	io.recvuntil('Hello Cryptographer, please enter the coefficients of the quadratic equation to proceed, hint: ')
	buf = io.recvline().decode().strip().split(' ')[-1]
	print(buf)
	x = float(buf)
	print(x)
	a = 10**17
	b = 10**17
	c = int(-a*x**2-b*x)
	print(a)
	print(b)
	print(c)
	io.sendlineafter('a: ',str(a))
	io.sendlineafter('b: ',str(b))
	io.sendlineafter('c: ',str(c))
	
print(io.recvall())
