import sys
import itertools as it

# 무방향 그래프, 가중치 방향 그래프 출력하기

sys.stdin = open("input.txt", 'r')

n, m = map(int, input().split())
g = [[0] * (n+1) for _ in range(n+1)]
# 간선정보 읽어서 적용
for i in range(m):
    a, b, c = map(int, input().split())
    g[a][b] = c

for i in range(1, n+1):
    for j in range(1, n+1):
        print(g[i][j], end=' ')
    print()