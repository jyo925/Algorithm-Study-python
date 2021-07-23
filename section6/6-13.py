import sys

# 경로 탐색(DFS)
# 방문 노드는 체크

sys.stdin = open("input.txt", 'r')

n, m = map(int, input().split())
g = [[0] * (n + 1) for _ in range(n + 1)]
# 간선정보 읽어서 행렬 생성
for i in range(m):
    a, b = map(int, input().split())
    g[a][b] = 1


def DFS(x):
    global cnt
    if x == n:
        cnt += 1
        print(path[:])
        return
    else:
        ch[x] = 1
        for j in range(1, n + 1):
            if ch[j] == 0 and g[x][j] == 1:
                path.append(j)
                DFS(j)
                path.pop()
        ch[x] = 0


cnt = 0
path = []
path.append(1)
ch = [0] * int(n + 1)
DFS(1)
print(cnt)
