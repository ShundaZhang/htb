import matplotlib.pyplot as plt
import pyshark

mousePosX = 0
mousePosY = 0

X = []
Y = []

f = pyshark.FileCapture('mitm.log', display_filter="btl2cap")

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
		key = []
		key.append(modify)
		for i in range(3, 3+6):
			key.append(int(data[i],16))
		#print(key)

#print(X)
#print(Y)
#plt.plot(X, Y)
#plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(X, Y)
plt.show()
