import sys
from collections import deque

# 송아지 찾기(BFS : 상태트리탐색)

# sys.stdin = open("input.txt", 'r')

MAX = 10000
ch = [0] * (MAX + 1)  # 방문 여부 체크
dis = [0] * (MAX + 1)  # 거리 기록

n, m = map(int, input().split())
ch[n] = 1
dis[n] = 0
dQ = deque()
dQ.append(n)

while dQ:
    now = dQ.popleft()
    if now == m:
        break

    for next in (now - 1, now + 1, now + 5):
        if 0 < next <= MAX and ch[next] == 0:
            dQ.append(next)
            ch[next] = 1
            dis[next] = dis[now] + 1


print(dis[m])