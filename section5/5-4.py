import sys
# 후위식 연산
sys.stdin = open("input.txt", 'r')

s = input()
stack = []

for x in s:
    if x.isdecimal():
        stack.append(x)
    else:
        tmp1 = stack.pop()
        tmp2 = stack.pop()
        stack.append(eval(str(tmp2) + x + str(tmp1)))


print(stack.pop())


