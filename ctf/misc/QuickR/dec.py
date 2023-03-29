from pwn import *
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import qrtools
import re

def qrimage( lines, fname ):
	font = ImageFont.truetype('DejaVuSansMono.ttf')
	image = Image.new('1', (102,102), 1)
	draw = ImageDraw.Draw(image)
	y = 0
	for line in lines:
		line = line.decode('utf-8', 'backslashreplace')
		line = re.sub(r'^\s*', '', line)
		line = re.sub(r'\[41m \[0m', '*', line)
		line = re.sub(r'\[7m \[0m', '-', line)

		x = 0
		for c in line:
			if c == '*':
				draw.point((x,y), 0)
			x += 1

		y += 1
		draw = ImageDraw.Draw(image)
	image.save(fname)

def qrdecode( fname ):
	ret = ''
	qr = qrtools.QR()
	if qr.decode(fname):
		ret = qr.data
	print(f'{ret}')
	return ret

def calc( f ):
	f = re.sub('x', '*', f)
	f = re.sub('=', '', f)
	f = re.sub(r'^\s*', '', f)
	f = re.sub(r'\s*$', '', f)
	print(f'{f}')
	ret = eval(f)
	print(f'{ret}')
	return ret

ip, port = '134.209.185.255', 30494
io = remote(ip, port)

context.log_level = 'debug'

io.recvuntil('3 seconds!')
'''
buf = io.recvuntil('Decoded string:').decode()

a = buf.split('\n')
print(a)
print(len(a))
#58
#QR code lines == 58 - 7 == 51
'''
io.recvlines(3)
qrbuf = io.recvlines(51)

#print(qrbuf)
imagename = 'qr.png'
qrimage(qrbuf, imagename)
f = qrdecode(imagename)
s = calc(f)

io.recvuntil('Decoded string:')
io.sendline(str(s).encode())
print(io.recvall())

