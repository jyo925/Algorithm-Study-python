import sys

# sys.stdin = open("input.txt", 'r')

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

m = int(input())
# rotation 행h 방향t 개수k
for i in range(m):
    h, t, k = map(int, input().split())
    if t == 0:
        for _ in range(k):
            data[h - 1].append(data[h - 1].pop(0))
    if t == 1:
        for _ in range(k):
            data[h - 1].insert(0, data[h - 1].pop())

res = 0
s = 0
e = n - 1

# 0,1,2,3,4
for i in range(n):
    for j in range(s, e + 1):
        res += data[i][j]

    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(res)
