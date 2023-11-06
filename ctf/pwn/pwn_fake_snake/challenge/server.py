#!/usr/bin/env python

from _ctypes import PyObj_FromPtr

storage = {}
commands = f'''
Zero: {id(0)}
0) Add To Store
1) Remove From Store
2) Load Address
'''.strip()

while True:
    print(commands)
    match(input('Selection:')):
        case '0':
            inp = input('To Add:')
            storage[id(inp)] = inp
            print(id(inp))
            del inp
        case '1':
            addr = input('To Remove:')
            if addr.isdecimal() and int(addr) in storage:
                del storage[int(addr)]
        case '2':
            addr = input('To Load:')
            if addr.isdecimal():
                print(PyObj_FromPtr(int(addr)))
            else:
                print('Invalid Address')
