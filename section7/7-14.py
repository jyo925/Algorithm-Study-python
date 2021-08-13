import sys
from collections import deque

# 안전영역(DFS)


sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10 ** 9)
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
# n = int(input())
# island = [list(map(int, input().split())) for _ in range(n)]
# res = []
# Q = deque()
#
# for h in range(100):
#     print(h)
#     ch = [[0] * n for _ in range(n)]
#     cnt = 0
#     for i in range(n):
#         for j in range(n):
#             if island[i][j] > h and ch[i][j] == 0:
#                 ch[i][j] = 1
#                 Q.append((i, j))
#                 while Q:
#                     tmp = Q.popleft()
#                     for k in range(4):
#                         x = tmp[0] + dx[k]
#                         y = tmp[1] + dy[k]
#                         if x < 0 or x >= n or y < 0 or y >= n or island[x][y] <= h:
#                             continue
#                         Q.append((x, y))
#                 cnt += 1
#
#     res.append(cnt)
#
# print(res)
# print(cnt)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(x, y, h):
    ch[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and board[xx][yy] > h:
            DFS(xx, yy, h)


if __name__ == "__main__":
    n = int(input())
    cnt = 0
    res = 0
    board = [list(map(int, input().split())) for _ in range(n)]

    # 높이 0부터
    for h in range(100):
        ch = [[0] * n for _ in range(n)]
        cnt = 0
        for i in range(n):
            for j in range(n):
                if ch[i][j] == 0 and board[i][j] > h:
                    cnt += 1
                    DFS(i, j, h)
        res = max(res, cnt)

        if cnt == 0:  # 최대 높이가 9인데 h가 9라면 cnt는 이때부터 0임(종료조건 성립)
            break

print(res)
