import sys

# 사다리 타기(DFS)
# 답에서 부터 거꾸로 출발하는 코드
sys.stdin = open("input.txt", 'r')

dx = [0, 0, -1]
dy = [-1, 1, 0]


def DFS(x, y):
    if x == 0:
        print(y)
        sys.exit()

    for k in range(3):
        xx = x + dx[k]
        yy = y + dy[k]
        if 0 <= xx < 10 and 0 <= yy < 10 and ladder[xx][yy] == 1:
            ladder[xx][yy] = 0
            DFS(xx, yy)


if __name__ == "__main__":
    goal = 2
    ladder = [list(map(int, input().split())) for _ in range(10)]

    # 시작 지점 찾기
    for i in range(10):
        if ladder[9][i] == goal:
            DFS(9, i)

