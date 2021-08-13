import sys
from collections import deque

# 섬나라 아일랜드(BFS)

sys.stdin = open("input.txt", "r")

dx = [-1, 0, 1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]

n = int(input())
island = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
Q = deque()

for i in range(n):
    for j in range(n):
        if island[i][j] == 1:
            island[i][j] = 0
            Q.append((i, j))

            while Q:
                tmp = Q.popleft()
                for k in range(8):
                    x = tmp[0] + dx[k]
                    y = tmp[1] + dy[k]
                    if x < 0 or x >= n or y < 0 or y >= n or island[x][y] == 0:
                        continue
                    island[x][y] = 0
                    Q.append((x, y))
            cnt += 1

print(cnt)
