#!/usr/bin/python3

from pwn import *

def change_opt(opt):
    result = []  
    stack = []  
    item_lists = opt.split(' ')
    for item in item_lists:
        if item.isdigit() or '.' in item:
            result.append(item)
        else:
            if len(stack) == 0:     
                stack.append(item)
            #elif item in '*/(':   
            elif item in '+(':   
                stack.append(item)
            elif item == ')':
                t = stack.pop()
                while t != '(':
                    result.append(t)
                    t = stack.pop()
            #elif item in '+-' and stack[-1] in '*/':
            elif item in '*' and stack[-1] in '+':
                if stack.count('(') == 0:
                    while stack:
                        result.append(stack.pop())
                else: 
                    t = stack.pop()
                    while t != '(':
                        result.append(t)
                        t = stack.pop()
                    stack.append('(')
                stack.append(item)
            else:
                stack.append(item)
    while stack:
        result.append(stack.pop())
    return result

def get_value(follow):
    num = []
    #base_opt = ['+', '-', '*', '/']
    base_opt = ['+', '*']
    # print(follow)
    for j in follow:
        if j.isdigit() or '.' in j:
            #num.append(float(j))
            num.append(int(j))
        if j in base_opt:
            num2 = num.pop()
            num1 = num.pop()
            res=method(num1,num2,j)
            num.append(res)
    return num[0]

def method(num1,num2,j):
    if j == "+":
        res=num1 + num2
    elif j == "-":
        res=num1 - num2
    elif j == "*":
        res=num1 * num2
    else:
        res=num1 / num2
    return res

context.log_level = 'debug'

ip, port = '139.59.174.176', 30781
io = remote(ip, port)

while True:
    io.recvuntil(']: ')
    buf = io.recvline()
    print(buf.decode())
    print(buf.decode()[:-5])
    s = buf.decode()[:-5]
    s = s.replace('(', '( ')
    s = s.replace(')', ' )')
    print(s)
    result=change_opt(s)
    io.sendline(str(get_value(result)))

#HTB{tH0s3_4r3_s0m3_k1llEr_m4th_5k1llz}
