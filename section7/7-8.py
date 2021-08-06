import sys
from collections import deque

# 사과나무(BFS)
# 방향 탐색
sys.stdin = open("input.txt", 'r')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ch = [[0] * n for _ in range(n)]  # 방문 체크
total = 0  # 총합 (답)
Q = deque()
ch[n // 2][n // 2] = 1  # 중앙지점 방문체크
total += a[n // 2][n // 2]
Q.append((n // 2, n // 2))
L = 0


while True:
    if L == n // 2:
        break
    size = len(Q)
    # 큐에 들어있는 원소 개수만큼 반복해서 4방향 탐색
    for i in range(size):
        tmp = Q.popleft()
        for j in range(4):
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if ch[x][y] == 0:
                total += a[x][y]
                ch[x][y] = 1
                Q.append((x, y))
    L += 1

print(total)
