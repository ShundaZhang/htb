from PIL import Image

png1 = 'intercepted.png'
png0 = 'original.png'

image1 = Image.open(png1)
image0 = Image.open(png0)

w, h = image1.size
#print(w, h)


for i in range(w):
	for j in range(h):
		p1 = image1.getpixel((i, j))
		p0 = image0.getpixel((i, j))
		if (p1 != p0):
			print(i, j)


