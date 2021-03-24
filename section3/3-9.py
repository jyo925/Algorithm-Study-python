import sys

# sys.stdin = open("input.txt", 'r')

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

data.insert(0, [0] * n)
data.append([0] * n)
for i in data:
    i.insert(0, 0)
    i.insert(len(i), 0)

d = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def check(x, y):
    for k in d:
        if data[x][y] <= data[x + k[0]][y + k[1]]:
            return False
    return True


cnt = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if check(i, j):
            cnt += 1
            j += 1

print(cnt)