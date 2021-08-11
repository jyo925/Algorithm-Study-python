import sys

# 등산경로(DFS)

sys.stdin = open("input.txt", 'r')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(x, y):
    global cnt

    if x == ex and y == ey:
        cnt += 1

    else:
        for i in range(4):
            tmp_x = x + dx[i]
            tmp_y = y + dy[i]
            if 0 <= tmp_x < n and 0 <= tmp_y < n \
                    and check[tmp_x][tmp_y] == 0\
                    and board[x][y] < board[tmp_x][tmp_y]:
                check[tmp_x][tmp_y] = 1
                DFS(tmp_x, tmp_y)
                check[tmp_x][tmp_y] = 0


if __name__ == "__main__":
    n = int(input())
    # board = [list(map(int, input().split())) for _ in range(n)]
    check = [[0] * n for _ in range(n)]
    board = [[0] * n for _ in range(n)]
    cnt = 0
    # check[0][0] = 1
    max = -2147000000
    min = 2147000000
    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(n):
            # 가장 낮은 높이를 start 지점으로 설정
            if tmp[j] < min:
                min = tmp[j]
                sx = i
                sy = j
            # 도착 지점 설정
            if tmp[j] > max:
                max = tmp[j]
                ex = i
                ey = j
            board[i][j] = tmp[j]
    check[sx][sy] = 1

    DFS(0, 0)
    print(cnt)
