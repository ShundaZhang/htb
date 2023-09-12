import csv
import math
import random
from secret import getFlagLocation

arr = []
with open('grid.csv') as grid:
    for x in csv.reader(grid):
        arr.append(x)
        pass

def getDistance(x,y,x2,y2):
    return math.sqrt(math.pow(x - x2,2) + math.pow(y - y2,2))

def cap(num):
    if num > 99:
        return 99
    if num < 0:
        return 0
    return num

def createCoords(x,y):
    x1 = random.randint(-7,7)
    y1 = random.randint(-7,7)
    x2 = random.randint(-7,7)
    y2 = random.randint(-7,7)
    x3 = random.randint(-7,7)
    y3 = random.randint(-7,7)

    p1 = [cap(x1 + x), cap(y1 + y)]
    p2 = [cap(x2 + x), cap(y2 + y)]
    p3 = [cap(x3 + x), cap(y3 + y)]

    val1 = arr[p1[0]][p1[1]]
    val2 = arr[p2[0]][p2[1]]
    val3 = arr[p3[0]][p3[1]]

    distances = [(val1,getDistance(x,y,p1[0], p1[1])),(val2,getDistance(x,y,p2[0], p2[1])),(val3,getDistance(x,y,p3[0], p3[1])),(f"{val1}{val2}",getDistance(p1[0], p1[1],p2[0], p2[1])),(f"{val2}{val3}",getDistance(p2[0], p2[1],p3[0], p3[1])),(f"{val1}{val3}",getDistance(p1[0], p1[1],p3[0], p3[1]))]
    return distances

def createTriangulation():
    with open("out1.csv",'w') as out:
        writer = csv.writer(out)
        for coord in getFlagLocation():
            for val, dist in createCoords(coord[0],coord[1]):
                writer.writerow([val,dist])

def main():
    createTriangulation()

if __name__ == "__main__":
    main()
