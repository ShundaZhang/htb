'''
void encrypt(longlong param_1,ulonglong param_2)

{
  undefined8 local_17;
  undefined2 local_f;
  undefined local_d;
  int local_c;

  local_17 = 0x4345535245505553;
  local_f = 0x5255;
  local_d = 0x45;
  for (local_c = 0; (ulonglong)(longlong)local_c < param_2; local_c = local_c + 1) {
    *(char *)(param_1 + local_c) =
         *(char *)((longlong)&local_17 + (ulonglong)(longlong)local_c % 0xb) +
         *(char *)(param_1 + local_c);
  }
  return;
}
'''

from pwn import *

key = p64(0x4345535245505553)+p16(0x5255)+p8(0x45)

len_key = 0xb

fname = 'login.xlsx.enc'
with open(fname, 'rb') as f:
	buf = f.read()

flag = []
dec_buf = b''
for i in range(len(buf)):
	#print(buf[i])
	#print(key[i%len_key])
	x = buf[i] - key[i%len_key]
	flag.append(x)
	if x < 0:
		x += 256
	dec_buf += x.to_bytes(1,'big')

#print(flag)

fout = 'login.xlsx'
with open(fout, 'wb') as f:
	f.write(dec_buf)

'''
print out the orignal integers, and goto https://gchq.github.io/CyberChef/
From Decimal, and download the file as download.xlsx

Or dump the data to xlsx file directly, but pay attention that use int.to_bytes, not chr().encode(), because in python3, > 128 char can be convert to more than one bytes unicode!!

HTB{M4lW4R3_4n4LY5I5_IN73r357iN9_57uFF}
'''
