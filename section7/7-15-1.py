import sys
from collections import deque

# 토마토(BFS 활용)
# 다른 풀이
# board와 똑같은 배열로 날짜를 표기하는 dis 배열을 추가로 사용
# 1. m*n for문으로 익은 토마토를 큐에 삽입한다.
# 2. 익은 토마토를 큐에서 하나씩 꺼내서 네 방향 체크해서 1로 변경 후 큐에 삽입, dis 값(익는데 걸린 날짜)도 익은 토마토의 값 + 1 로 업데이트
# 큐가 빌 때까지 2번 수행
# 3. dis를 읽어서 최대값을 찾으면 됨

sys.stdin = open("input.txt", "r")
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
sys.setrecursionlimit(10 ** 6)
# m이 행
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
Q = deque()
dis = [[0] * n for _ in range(m)]

for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            Q.append((i, j))

while Q:
    x, y = Q.popleft()
    for k in range(4):
        xx = x + dx[k]
        yy = y + dy[k]
        if 0 <= xx < m and 0 <= yy < n and board[xx][yy] == 0:
            board[xx][yy] = 1
            dis[xx][yy] = dis[x][y] + 1
            Q.append((xx, yy))

flag = 1
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            flag = 0

result = 0
if flag == 1:
    for i in range(m):
        for j in range(n):
            if dis[i][j] > result:
                result = dis[i][j]
    print(result)
else:
    print(-1)
