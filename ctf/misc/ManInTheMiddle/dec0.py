#!/usr/bin/python

import matplotlib.pyplot as plt
import pyshark

mousePosX = 0
mousePosY = 0

X = []
Y = []

#USB HID Keyboard scan codes as per USB spec 1.11
#https://gist.github.com/MightyPork/6da26e382a7ad91b5496ee55fdc73db2?permalink_comment_id=4339074
k={
	0x04:"A",
	0x05:"B",
	0x06:"C",
	0x07:"D",
	0x08:"E",
	0x09:"F",
	0x0a:"G",
	0x0b:"H",
	0x0c:"I",
	0x0d:"J",
	0x0e:"K",
	0x0f:"L",
	0x10:"M",
	0x11:"N",
	0x12:"O",
	0x13:"P",
	0x14:"Q",
	0x15:"R",
	0x16:"S",
	0x17:"T",
	0x18:"U",
	0x19:"V",
	0x1a:"W",
	0x1b:"X",
	0x1c:"Y",
	0x1d:"Z",
	0x1e:"1",
	0x1f:"2",
	0x20:"3",
	0x21:"4",
	0x22:"5",
	0x23:"6",
	0x24:"7",
	0x25:"8",
	0x26:"9",
	0x27:"0",
	0x2d:"_",
	0x2f:"{",
	0x30:"}"
}

f = pyshark.FileCapture('mitm.log', display_filter="btl2cap")
flag = ''
for p in f:
	data = p['btl2cap'].payload.split(":")
	proto = int(data[0],16)
	mouse = int(data[1],16)
	if proto == 0xa1 and mouse == 2:
		press = int(data[2],16)
		x_disp = int(data[3],16)
		y_disp = int(data[4],16)

		# disp is a signed char
		if x_disp > 127:
			x_disp -= 256
		if y_disp > 127:
			y_disp -= 256

		mousePosX += x_disp
		mousePosY += y_disp
		
		if press:
			X.append(mousePosX)
			Y.append(-mousePosY)
	
	elif proto == 0xa1 and mouse == 1:
		modify = int(data[2],16)
		#a1:01:00:00:07:00:00:00:00
		#a1:01:00:00:00:00:00:00:00
		#a1:01:02:00:00:00:00:00:00
		try:
			if modify == 0x02:
				flag += k[int(data[4],16)]
			else:
				flag += k[int(data[4],16)].lower()
		except:
			pass

print(flag)

#print(X)
#print(Y)
#plt.plot(X, Y)
#plt.show()

#fig = plt.figure()
#ax1 = fig.add_subplot(111)
#ax1.scatter(X, Y)
#plt.show()
