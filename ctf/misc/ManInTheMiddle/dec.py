import matplotlib.pyplot as plt
import pyshark

mousePosX = 0
mousePosY = 0

X = []
Y = []

f = pyshark.FileCapture('mitm.log', display_filter="btl2cap")

for p in f:
    data = p['btl2cap'].payload.split(":")
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

fig = plt.figure()
ax1 = fig.add_subplot()
ax1.scatter(X, Y)
plt.show()
