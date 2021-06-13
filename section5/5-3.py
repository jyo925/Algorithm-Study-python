import sys
# 중위표기식 -> 후위표기식으로 만들기
# 피연산자(숫자)면 그대로 출력
# 연산자면 스택에 삽입
# *, /와 -, +와 (, )인 경우를 생각
sys.stdin = open("input.txt", 'r')

s = input()
stack = []
res = ''


for x in s:
    if x.isdecimal():
        res += x
    else:
        if x == '(':
            stack.append(x)
        elif x == '*' or x == '/':
            # 동일 우선순위가 스택에 있으면 먼저 처리
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            # 더하기나 빼기는 연산순위 마지막으로 스택에 있는 것을 다 꺼내기
            # 여는 괄호 전까지만
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()

while stack:
    res += stack.pop()

print(res)


