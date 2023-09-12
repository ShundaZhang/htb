#!/bin/python
import csv
import math

def getDistance(x,y,x2,y2):
    return math.sqrt(math.pow(x - x2,2) + math.pow(y - y2,2))


def cap(num):
    #Restrict to a 100x100 table
    if num > 99:
        return 99
    if num < 0:
        return 0
    return num


arr=[]
with open('grid.csv') as grid:
    for x in csv.reader(grid):
        arr.append(x)
        pass
        
out = open("out.csv", "r").read().split("\n")

	        
for c in range(22):
	print("--------------------")
	possibles=[]
	for y in range(100):
		for x in range(100):
			isPossible=True
			editedValChoors=[]
			for k in range(3):
				isPossibleB=False
				line=6*c+k
				value=out[line].split(",")[0]
				distGoal=float(out[line].split(",")[1])
				for dX in range(-7,8):
					for dY in range(-7,8):
						xEditedValue=cap(x+dX)
						yEditedValue=cap(y+dY)	
						calcDist=getDistance(xEditedValue,yEditedValue,x,y)
						
						if(distGoal==calcDist and arr[yEditedValue][xEditedValue]==value):
							isPossibleB=True
							editedValChoors.append([k,xEditedValue,yEditedValue])
				if(isPossibleB==False):
					isPossible=False
			if(isPossible):
				possibles.append([arr[y][x],editedValChoors])

	for p in range(len(possibles)):	
		for k in range(3,6):
			isPossible=False
			line=6*c+k
			goalDist=float(out[line].split(",")[1])
			for pA in range(len(possibles[p][1])):
				xA=possibles[p][1][pA][1]
				yA=possibles[p][1][pA][2]
				for pB in range(len(possibles[p][1])):
					xB=possibles[p][1][pB][1]
					yB=possibles[p][1][pB][2]
					calcDist=getDistance(xA,yA,xB,yB)
					if(calcDist==goalDist):
						if(k-3==0):
							if(possibles[p][1][pA][0]==0 and possibles[p][1][pB][0]==1):
								isPossible=True
						if(k-3==1):
							if(possibles[p][1][pA][0]==1 and possibles[p][1][pB][0]==2):
								isPossible=True
						if(k-3==2):
							if(possibles[p][1][pA][0]==0 and possibles[p][1][pB][0]==2):
								isPossible=True

		if(isPossible):
			print(possibles[p][0])

'''
--------------------
H
--------------------
T
--------------------
B
e
--------------------
{
--------------------
s
--------------------
Q
:
--------------------
U
--------------------
H
@
--------------------
u
r
--------------------
3
--------------------
s
s
--------------------
_
--------------------
R
--------------------
_
J
--------------------
^
4
o
--------------------
_
--------------------
N
--------------------
E
3
--------------------
:
W
r
--------------------
v
D
[
--------------------
$
B
--------------------
n
}


HTB{sQU@r3s_R_4_N3rD$}
'''
