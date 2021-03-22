import sys

# sys.stdin = open("input.txt", 'r')
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
