#!/usr/bin/python3

from pwn import *
from Crypto.Cipher import Salsa20 

'''
https://filipedeluna.medium.com/htb-rauth-reversing-write-up-5f7b7393a1a7

Salsa20

    *__ptr = 0xb15f0505;
    __ptr[1] = 0xd5a829a3;
    __ptr[2] = 0x56f5d958;
    __ptr[3] = 0xf331cba6;
    __ptr[4] = 0x312a4324;
    __ptr[5] = 0x72ec9dc9;
    __ptr[6] = 0x6fb63ee3;
    __ptr[7] = 0xf91bad62;


    RSP  0x7fffffffdf70 ◂— 'expaef39f4f20e76e33bnd 3d4c270a3'


    00:0000│ rsp 0x7fffffffdf68 —▸ 0x55555540675e (rauth::main+766) ◂— test al, al
01:0008│     0x7fffffffdf70 ◂— 'expaef39f4f20e76e33bnd 3d4c270a3'
02:0010│     0x7fffffffdf78 ◂— 'f4f20e76e33bnd 3d4c270a3'
03:0018│     0x7fffffffdf80 ◂— 'e33bnd 3d4c270a3'
04:0020│     0x7fffffffdf88 ◂— 'd4c270a3'
05:0028│     0x7fffffffdf90 ◂— 0x0
06:0030│     0x7fffffffdf98 ◂— 0x6635326479622d32 ('2-byd25f')
07:0038│     0x7fffffffdfa0 ◂— 0x3865383333626434 ('4db338e8')

pwndbg> x 0x7fffffffdfa0
0x7fffffffdfa0: 0x33626434
pwndbg> x/20 0x7fffffffdfa0
0x7fffffffdfa0: 0x33626434      0x38653833      0x30316231      0x6b206574
0x7fffffffdfb0: 0x5564fe60      0x00005555      0x00000006      0x00000000
0x7fffffffdfc0: 0x00000006      0x00000000      0x5564fdf0      0x00005555
0x7fffffffdfd0: 0x00000008      0x00000000      0x00000006      0x00000000
0x7fffffffdfe0: 0x5564fe10      0x00005555      0x00000006      0x00000000

'''

enc = p32(0xb15f0505) + p32(0xd5a829a3) + p32(0x56f5d958) + p32(0xf331cba6) + p32(0x312a4324) + p32(0x72ec9dc9) + p32(0x6fb63ee3) + p32(0xf91bad62)

#expaef39f4f20e76e33bnd 3d4c270a32-byd25f4db338e8 p32(0x30316231) p32(0x6b206574)
#expa ef39f4f20e76e33b nd 3 d4c270a3 2-by d25f4db338e81b10 te k
key = b'ef39f4f20e76e33bd25f4db338e81b10'
iv = b'd4c270a3'

cipher = Salsa20.new(key=key,nonce=iv)
password = cipher.decrypt(enc)
print(password)

#TheCrucialRustEngineering@2021;)
#HTB{I_Kn0w_h0w_t0_5al54}
