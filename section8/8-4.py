import sys

# 최대 부분 증가수열(LIS)

sys.stdin = open("input.txt", 'r')

n = int(input())
seq = list(map(int, input().split()))
seq.insert(0, 0)
dy = [0] * (n + 1)
dy[1] = 1
res = 0

for i in range(2, n + 1):
    max = 0
    for j in range(i - 1, 0, -1):
        if seq[i] > seq[j] and dy[j] > max:
            max = dy[j]

    dy[i] = max + 1
    if dy[i] > res:
        res = dy[i]

print(res)
