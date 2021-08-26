import sys

# 돌다리 건너기(보텀업)

sys.stdin = open("input.txt", 'r')


n = int(input())
dy = [0] * (n+2)
dy[1] = 1
# dy[2] = 2

for i in range(3, n+2):
    if i ==2 or i== 4:
        dy[i] = 0
        continue
    dy[i] = dy[i-1] + dy[i-2]

print(dy[8])
