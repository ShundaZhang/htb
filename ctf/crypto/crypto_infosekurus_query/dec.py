#Bad RSA Keys
#A method to recover potential plaintexts when bad RSA keys were used
#https://medium.com/@g2f1/bad-rsa-keys-3157bc57528e

from pwn import *
import gmpy2
from Crypto.Util.number import long_to_bytes

#context.log_level = 'debug'

N = 96124936107896748280555244677021991330091778649135119790286533059582754409293601619525608937362904170585046388534482094091790568122866360316740693418876264680551778543440000535075643338759767637391693271627644627735703513501276657327234250653312367333508135208249266632071094632385510113463482633032902002209
phi = 96124936107896748280555244677021991330091778649135119790286533059582754409293601619525608937362904170585046388534482094091790568122866360316740693418876244909857319694820595566002064612532239556729264541411304166794719906273078548635013448269328260390344716890710955831745947175474039259985922959198890019520

ip, port = '83.136.255.81', 54011
io = remote(ip, port)

io.recvuntil('::')
io.sendline('{"option":"1"}')
io.recvuntil('::')
io.sendline('{"choice":6}')

io.recvline()
buf = io.recvline().decode().strip()
c = int(buf.split(': ')[-1][:-1])

e = 8192
k = 1

'''
#sage
while gcd(phi/k, e) != 1:
	k = k*gcd(phi/k, e)

print(k)
'''
k = 64

R = []
max = 4096
for a in range(1, max):
	r = pow(a, phi//k, N)
	R.append(r)

#print(R)

d = gmpy2.invert(e, phi//k)
g = pow(c, d, N)

for l in R:
    m = (l*g) % N
    if pow(m, e, N) == c:
        try:
            passcode = long_to_bytes(m).decode()
            print(passcode)
            break
        except:
            pass

print(passcode)

s='+%2$?!_8*469'
for i1 in s:
    for i2 in s:
        for i3 in s:
            print(i1+i2+i3)
            for i4 in s:
                for i5 in s:
                    t = i1+i2+i3+i4+i5
                    #print(t)
                    io.recvuntil('::')
                    io.sendline('{"option":"3"}')
                    io.recvuntil('::')
                    io.sendline('{"passcode":"'+passcode.encode().hex()+'"}')
                    io.recvuntil('::')
                    io.sendline('{"answer":"6666"}')
                    io.recvuntil('::')
                    io.sendline('{"token":"'+t.encode().hex()+'"}')
                    io.recvline()
                    buf = io.recvline()
                    if b'here you go' in buf:
                        print(buf)
                        break

#HTB{th3_ru1n5_0f_th3_d4y_p41nt3d_w1th_4_sc4r}
