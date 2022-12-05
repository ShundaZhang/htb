'''
xxd flag.enc
00000000: 5a35 b162 00f5 3e12 c0bd 8d16 f0fd 7599  Z5.b..>.......u.
00000010: faef 399a 4b96 21a1 4316 2371 65fb 274b  ..9.K.!.C.#qe.'K

  tVar2 = time((time_t *)0x0);
  local_40 = (uint)tVar2;
  srand(local_40);
  for (local_38 = 0; local_38 < (long)local_28; local_38 = local_38 + 1) {
    iVar1 = rand();
    *(byte *)((long)local_20 + local_38) = *(byte *)((long)local_20 + local_38) ^ (byte)iVar1;
    local_3c = rand();
    local_3c = local_3c & 7;
    *(byte *)((long)local_20 + local_38) =
         *(byte *)((long)local_20 + local_38) << (sbyte)local_3c |
         *(byte *)((long)local_20 + local_38) >> 8 - (sbyte)local_3c;
  }
  local_18 = fopen("flag.enc","wb");
  fwrite(&local_40,1,4,local_18);
  fwrite(local_20,1,local_28,local_18);
  fclose(local_18);

'''

from ctypes import CDLL

seed = 0x62b1355a
enc = "\x00\xf5\x3e\x12\xc0\xbd\x8d\x16\xf0\xfd\x75\x99\xfa\xef\x39\x9a\x4b\x96\x21\xa1\x43\x16\x23\x71\x65\xfb\x27\x4b"

libc = CDLL("libc.so.6")

libc.srand(seed)

r1 = []
r2 = []
for i in range(len(enc)):
	r1.append(libc.rand()&0xFF)
	r2.append(libc.rand()&7)

flag = ''
f = ''
for i in range(len(enc)):
	f += chr(ord(enc[i]) >> r2[i] | (ord(enc[i]) << 8-r2[i]) & 0xFF)
	flag += chr(ord(f[i])^r1[i])

print flag
