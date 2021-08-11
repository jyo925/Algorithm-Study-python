import sys

# 미로탐색(DFS)

sys.stdin = open("input.txt", 'r')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(x, y):
    global cnt

    if x == 6 and y == 6:
        cnt += 1

    else:
        for i in range(4):
            tmp_x = x + dx[i]
            tmp_y = y + dy[i]
            if 0 <= tmp_x <= 6 and 0 <= tmp_y <= 6 and board[tmp_x][tmp_y] == 0:
                board[tmp_x][tmp_y] = 1
                DFS(tmp_x, tmp_y)
                board[tmp_x][tmp_y] = 0


if __name__ == "__main__":
    board = [list(map(int, input().split())) for _ in range(7)]
    cnt = 0
    board[0][0] = 1
    DFS(0, 0)
    print(cnt)
