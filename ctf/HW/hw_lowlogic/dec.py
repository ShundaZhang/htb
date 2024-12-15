with open('input.csv','r') as f:
    lines = f.readlines()

#print(lines)

xline = []

for i in range(1,len(lines),1):
    in1,in2,in3,in4 = lines[i].strip().split(',')
    x = (int(in1) and int (in2)) or (int(in3) and int(in4))
    xline.append(x)

#print(xline)
flag = ''
for i in range(0,len(xline),8):
    x = ''
    for j in range(8):
        x += str(xline[i+j])
    flag += chr(int(x,2))

print(flag)
#HTB{4_G00d_Cm05_3x4mpl3}
