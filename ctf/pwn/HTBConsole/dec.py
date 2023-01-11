from pwn import *

io = process('./htb-console')

elf = ELF('./htb-console')

print elf.got.puts
print elf.plt.puts
