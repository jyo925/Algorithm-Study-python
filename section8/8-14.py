import sys
from collections import deque

# 위상정렬(그래프 정렬)
# 들어오는 간선을 하나씩 제거하면서 순서를 찾으면 됨
# 각 노드마다 진입차수를 이용
# 진입차수가 0이면 작업을 바로 해도 된다는 것 => 큐 이용

sys.stdin = open("input.txt", 'r')

if __name__ == "__main__":
    n, m = map(int, input().split())
    orders = [[0] * (n + 1) for _ in range(n + 1)]
    degree = [0] * (n + 1)
    dQ = deque()

    for i in range(m):
        a, b = map(int, input().split())
        orders[a][b] = 1
        degree[b] += 1

    for i in range(1, n + 1):
        if degree[i] == 0:
            dQ.append(i)

    while dQ:
        x = dQ.popleft()
        print(x, end=' ')
        for i in range(1, n + 1):
            if orders[x][i] == 1:
                degree[i] -= 1
                if degree[i] == 0:
                    dQ.append(i)
