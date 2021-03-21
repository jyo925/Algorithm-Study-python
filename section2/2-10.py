import sys

sys.stdin = open("input.txt", "rt")
n = int(input())
score = list(map(int, input().split()))

total = [0] * (n + 1)
num = 0
for i in enumerate(score):
    if i[1] == 1:
        num += 1
    else:
        num = 0
    total[i[0]] = num

print(sum(total))
