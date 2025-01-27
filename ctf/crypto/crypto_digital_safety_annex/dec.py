from pwn import *
import gmpy2

context.log_level = 'debug'

ip,port = '94.237.63.109', 37864
io = remote(ip,port)

io.recvuntil('>')
io.sendline('4')

buf = io.recvuntil('[+] Test user log (y/n) : ')
p = int(buf.decode().split('\n')[6].split(' = ')[1])
q = int(buf.decode().split('\n')[7].split(' = ')[1])
g = int(buf.decode().split('\n')[8].split(' = ')[1])


io.sendline('y')
io.recvuntil('Enter your password : ')
io.sendline('5up3r_53cur3_P45sw0r6')

buf = io.recvuntil('>')
r = int(buf.decode().split('\n')[1].split('((')[6].split(',')[0])
s = int(buf.decode().split('\n')[1].split('((')[6].split(',')[1][1:-1])
h = int(buf.decode().split('\n')[1].split('((')[6].split(',')[2].split(')]')[0].split("'")[1], 16)

for k in range(65500, 10**6):
    if k%2000 == 0:
        print(k)
    if pow(g, k, p)%q == r:
        kx = k
        break

io.sendline('3')
io.recvuntil('Please enter the username who stored the message : ')
io.sendline('ElGamalSux')
io.recvuntil('Please enter the message\'s request id: ')
io.sendline('3')
io.recvuntil('Please enter the message\'s nonce value : ')
io.sendline(str(k))
io.recvuntil('[+] Please enter the private key: ')
pri = ((kx*s-h)*gmpy2.invert(r,q))%q
io.sendline(str(pri))
buf = io.recvall()
print(buf)

#HTB{1_Gu3ss_d54_15_N07_4s_s3CuR3_A5_1_7h0u647}
