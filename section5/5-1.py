import sys
# 가장 큰 수
sys.stdin = open("input.txt", 'r')

num, m = map(int, input().split())

# num을 문자로 바꾼 후에 map을 적용시켜야 함
num = list(map(int, str(num)))

stack = []
for x in num:
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)

if m != 0:
    stack = stack[:-m]

# while m != 0:
#     stack.pop()

res = ''.join(map(str, stack))
print(res)