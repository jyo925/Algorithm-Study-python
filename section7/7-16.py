import sys

# 사다리 타기(DFS)

sys.stdin = open("input.txt", 'r')

dx = [0, 0, 1]
dy = [-1, 1, 0]


def DFS(x, y):
    # print(i)
    if x > 9:
        return

    for k in range(3):
        xx = x + dx[k]
        yy = y + dy[k]
        if 0 <= xx < 10 and 0 <= yy < 10 and ladder[xx][yy] != 0 and check[xx][yy] == 0:
            # print("i는", i, "ladder[xx][yy]", xx, yy, ladder[xx][yy])
            check[xx][yy] = 1
            if ladder[xx][yy] == 2:
                print(i)
                sys.exit()
            break

        # print("수행")
    # check[xx][yy] = 1

    DFS(xx, yy)


if __name__ == "__main__":
    goal = 2

    ladder = [list(map(int, input().split())) for _ in range(10)]
    for i in range(10):
        check = [[0] * 10 for _ in range(10)]
        if ladder[0][i] == 1:
            DFS(0, i)
    # ch[5][5] = 1
    # if ch[5][5] == 0:
    #     print("dd")
    # print(ch)
