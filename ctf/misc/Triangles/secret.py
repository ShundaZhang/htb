import csv

f = "HTB{fake_flag_for_testing}"

arr = []
with open('grid.csv') as grid:
    for x in csv.reader(grid):
        arr.append(x)
        pass

flagLocation = list()
# Coordinates are all placeholder values
flagLocation.append([1,2]) # H
flagLocation.append([2,2]) # T
flagLocation.append([3,2]) # B
flagLocation.append([4,2]) # {
flagLocation.append([55,2]) # f
flagLocation.append([65,2]) # a
flagLocation.append([75,2]) # k
flagLocation.append([85,2]) # e
flagLocation.append([9,25]) # _
flagLocation.append([5,2]) # f
flagLocation.append([6,2]) # l
flagLocation.append([7,2]) # a
flagLocation.append([8,2]) # g
flagLocation.append([9,2]) # _
flagLocation.append([1,12]) # f
flagLocation.append([2,22]) # o
flagLocation.append([3,32]) # r
flagLocation.append([4,12]) # _
flagLocation.append([5,22]) # t
flagLocation.append([6,32]) # e
flagLocation.append([7,22]) # s
flagLocation.append([8,42]) # t
flagLocation.append([9,52]) # i
flagLocation.append([12,2]) # n
flagLocation.append([11,2]) # g
flagLocation.append([13,2]) # }

def getFlagLocation():
    return flagLocation

def checkFlag():
    for i in range(len(f)):
        if arr[flagLocation[i][0]][flagLocation[i][1]] != f[i]:
            print("error")
            pass
