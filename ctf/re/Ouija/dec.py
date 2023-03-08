'''
  local_78 = 0x6877644b7b544c5a;
  local_70 = 0x665f6b615f796661;
  local_68 = 0x6b6d7874675f6c67;
  local_60 = 0x616c7375;
  local_5c = 0x6667;
  local_5a = 0x7d;
'''
from pwn import *

f = p64(0x6877644b7b544c5a) + p64(0x665f6b615f796661) + p64(0x6b6d7874675f6c67) + p32(0x616c7375) + p16(0x6667) + p8(0x7d)
print f

#gcc -o dec dec.c
#./dec

#HTB{Sleping_is_not_obfuscation}
