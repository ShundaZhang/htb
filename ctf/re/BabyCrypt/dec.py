from pwn import *

f =  p64(0x6f0547480c35643f) + p64(0x28130304026f0446) + p64(0x5000f4358280e52) + p16(0x4d56)

print xor(f, xor('\x3f\x64\x35', 'HTB'))
