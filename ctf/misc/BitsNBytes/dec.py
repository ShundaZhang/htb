from PIL import Image
from Crypto.Util.number import long_to_bytes

png1 = 'intercepted.png'
png0 = 'original.png'

image1 = Image.open(png1)
image0 = Image.open(png0)

w, h = image1.size
#print(w, h)

index = []

for i in range(w):
	for j in range(h):
		p1 = image1.getpixel((i, j))
		p0 = image0.getpixel((i, j))
		if (p1 != p0):
			#print(i, j)
			index.append(j)

fb = ''
for i in range(416):
	if i in index:
		fb += '1'
	else:
		fb += '0'

print long_to_bytes(int(fb, 2)).decode('base64')
#HTB{1f_a_w00d_chuck_c0uld_chuck_w00d}
