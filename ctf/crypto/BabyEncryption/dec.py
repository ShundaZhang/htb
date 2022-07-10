'''
import string
from secret import MSG

def encryption(msg):
    ct = []
    for char in msg:
        ct.append((123 * char + 18) % 256)
    return bytes(ct)

ct = encryption(MSG)
f = open('./msg.enc','w')
f.write(ct.hex())
f.close()
'''

enc = '6e0a9372ec49a3f6930ed8723f9df6f6720ed8d89dc4937222ec7214d89d1e0e352ce0aa6ec82bf622227bb70e7fb7352249b7d893c493d8539dec8fb7935d490e7f9d22ec89b7a322ec8fd80e7f8921'

for i in range(0,len(enc),2):
	c = int(enc[i:i+2],16)
	for p in range(0x20, 0x7f, 1):
		if (123*p + 18)%256 == c:
			print chr(p),

#Th3 nucl34r w1ll 4rr1v3 0n fr1d4y.HTB{l00k_47_y0u_r3v3rs1ng_3qu4710n5_c0ngr475}
