from pwn import *
import os

ip, port = '142.93.32.153', 31494


while 1:
    io = remote(ip, port)
    for _ in range(10):
        io.recvuntil('Hello Cryptographer, please enter the coefficients of the quadratic equation to proceed, hint: ')
        buf = io.recvline().decode().strip().split(' ')[-1]
        #print(buf)
        x = float(buf)
        #print(x)
        a = 10**17
        b = 10**17
        c = int(-a*x**2-b*x)
        #print(a)
        #print(b)
        #print(c)
        io.sendlineafter('a: ',str(a))
        io.sendlineafter('b: ',str(b))
        io.sendlineafter('c: ',str(c))
        
    buf = io.recvall().decode().split()
    io.close()
    Gx = buf[11][1:-1]
    Gy = buf[12][:-1]
    Gnx = buf[15][1:-1]
    Gny = buf[16][:-1]
    p = buf[19]

    cmd = 'sage dec.sage ' + str(b) + ' ' + str(c) + ' ' + Gx + ' ' + Gy + ' ' + Gnx + ' ' + Gny + ' ' + p
    print(cmd)
    ret = os.system(cmd)
    if ret == 0:
        break


