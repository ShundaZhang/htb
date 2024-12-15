s = 'be284b240578f70a17fc0d11a1c3af0733c5fe6aa259d64eb0d4c533b882652820373843fc145a059f5f1919203738439f5f19195e9c7c7437a23d0f99b25a6133c5fe6a2037384337a23d0f33c5fe6a99b25a61b8826528fc145a059449e43ae9dfd706a259d64ecd4acd0c64edd85799b25a612abce922'

x = []
for i in range(0,len(s),8):
    x.append(int(s[i+6:i+8]+s[i+4:i+6]+s[i+2:i+4]+s[i:i+2],16))
    

print(x)

from ctypes import CDLL

libc = CDLL("libc.so.6")

flag = ''
for i in range(0x1d+1):
    for j in range(0x20,0x7f,1):
        libc.srand(j)
        if libc.rand() == x[i]:
            flag += chr(j)
            break

print(flag)
#HTB{r4nd_1s_sup3r_pr3d1ct4bl3}
