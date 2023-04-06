s = ''.join(['14 ', '* ', '(23 ', '+ ', '6 ', '+ ', '67 ', '* ', '30 ', '* ', '25)'])
print(s)

s = s.replace('(', '( ')
s = s.replace(')', ' )')
print(s)

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

if __name__ == '__main__':
    #opt = "9 + ( 3 - 1 ) * 3 + 10 / 2"
    opt = s
    result=change_opt(opt)
    print(get_value(result))
