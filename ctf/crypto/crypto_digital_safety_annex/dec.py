from pwn import *

ip,port = '94.237.58.87', 56603
io = remote(ip,port)

io.recvuntil('>')
io.sendline('4')

buf = io.recvuntil('[+] Test user log (y/n) : ')
print(buf.decode().split('\n'))

io.sendline('y')
io.recvuntil('Enter your password : ')
io.sendline('5up3r_53cur3_P45sw0r6')

buf = io.recvuntil('>')
nonce = buf.decode().split('\n')[1].split('((')[6].split(',')[2].split(')]')[0].split("'")[1]

print(nonce)
#print(hex(int(nonce,16)))

'''
for k in range(65500, 10**6):
    print(k)
    io.sendline('3')
    io.recvuntil('Please enter the username who stored the message : ')
    io.sendline('ElGamalSux')
    io.recvuntil('Please enter the message\'s request id: ')
    io.sendline('5')
    io.recvuntil('Please enter the message\'s nonce value : ')
    io.sendline(nonce)
    io.recvuntil('[+] Please enter the private key: ')
    io.sendline(str(k))
    buf = io.recvline()
    if 'Here is your super secret message' in buf:
        print(buf)
        break
    io.recvuntil('>')
'''
