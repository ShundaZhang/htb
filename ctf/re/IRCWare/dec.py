from pwn import *

s = '09071148207302682c6762023e367d1a1e351f072a1d3c0b712562577e30133b71072e'.decode('hex')

k = 'RJJ3DSCP'

'''
  if (((0x40 < bVar3) && (bVar3 < 0x5b)) && (bVar4 = bVar3 + 0x11, 0x5a < bVar4)) {
    bVar4 = bVar3 - 9;
  }
'''

key = ''

for i in range(len(k)):
	for x in range(0x20, 0x7f, 1):
		x1 = x
		if ( x > 0x40 and x < 0x5b ):
			x1 = x + 0x11
			if x1 > 0x5a:
				x1 = x - 9
		if x1 == ord(k[i]):
			key += chr(x)
			break

print key
print xor(s, key)
