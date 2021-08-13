import sys
from collections import deque

# 토마토(BFS 활용)
# 내 풀이 -> 매우 비효율적 주먹구구식
# sys.stdin = open("input.txt", "r")
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
sys.setrecursionlimit(10 ** 6)

m, n = map(int, input().split())
res = 0
board = [list(map(int, input().split())) for _ in range(n)]
Q = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            Q.append((i, j))

if len(Q) == 0:
    print(-1)

cnt = len(Q)
tq = []
while Q:
    tmp = Q.popleft()
    for k in range(4):
        xx = tmp[0] + dx[k]
        yy = tmp[1] + dy[k]
        if 0 <= xx < n and 0 <= yy < m and board[xx][yy] == 0:
            board[xx][yy] = 1
            tq.append((xx, yy))
    if len(Q) == 0:
        res += 1
        for a in tq:
            Q.append(a)
        tq = []

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            Q.append((i, j))
            
if len(Q) > 0:
    print(-1)
else:
    print(res-1)
