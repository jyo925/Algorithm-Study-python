import sys
from collections import deque

# 안전영역(BFS)

# sys.stdin = open("input.txt", "r")
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
sys.setrecursionlimit(10 ** 6)

n = int(input())
res = 0
board = [list(map(int, input().split())) for _ in range(n)]
Q = deque()

for h in range(100):
    ch = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if ch[i][j] == 0 and board[i][j] > h:
                Q.append((i, j))
                cnt += 1
                while Q:
                    tmp = Q.popleft()
                    for k in range(4):
                        xx = tmp[0] + dx[k]
                        yy = tmp[1] + dy[k]
                        if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and board[xx][yy] > h:
                            ch[xx][yy] = 1
                            Q.append((xx, yy))

    res = max(res, cnt)
    if cnt == 0:
        break

print(res)
