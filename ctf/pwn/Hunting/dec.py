#https://shakuganz.com/2021/07/14/hackthebox-hunting-write-up/
#https://fdlucifer.github.io/2021/01/27/hunting/

from pwn import *

context.arch = 'i386'
context.log_level = 'debug'

io = process('./hunting')
#ip, port = 
#io = remote(ip, port)

'''

'''

sc = asm()
#print len(sc)

io.sendline(sc)
print io.recvall()
