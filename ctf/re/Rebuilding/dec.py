'''
      local_14 = local_14 +
                 (uint)((byte)(encrypted[local_10] ^ key[local_10 % 6]) ==
                       *(byte *)((long)local_10 + *(long *)(param_2 + 8)));

void _INIT_1(void)

{
  puts("Preparing secret keys");
  key[0] = 'a';
  key[1] = 'l';
  key[2] = 'i';
  key[3] = 'e';
  key[4] = 'n';
  key[5] = 's';
  return;

'''

from pwn import *

encrypted = '\x29\x38\x2b\x1e\x06\x42\x05\x5d\x07\x02\x31\x10\x51\x08\x5a\x16\x31\x42\x0f\x33\x0a\x55\x00\x00\x15\x1e\x1c\x06\x1a\x43\x13\x59\x14'

#key = 'humans'
key = 'aliens'

print xor(encrypted, key)

#HTB{h1d1ng_c0d3s_1n_c0nstruct0r5}
