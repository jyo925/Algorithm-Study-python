import sys

# sys.stdin = open("input.txt", 'r')
# decimal은 0~9까지의 숫자를 확인
# digit 알파벳이 아닌 숫자 형태는 다 찾아줌(예를 들어 2^2)
input_text = input()

num = 0
for i in input_text:
    if i.isdecimal():
        num = (num * 10) + int(i)

print(num)

count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1

print(count)
