import sys

# 사다리 타기(DFS)
# 내 코드의 문제점: 모든 열을 확인하는 것은 비효율적-> 답에서 부터 거꾸로 출발하기
# sys.stdin = open("input.txt", 'r')

dx = [0, 0, 1]
dy = [-1, 1, 0]


def DFS(x, y):
    if x > 9:
        return

    for k in range(3):
        xx = x + dx[k]
        yy = y + dy[k]
        if 0 <= xx < 10 and 0 <= yy < 10 and ladder[xx][yy] != 0 and check[xx][yy] == 0:
            check[xx][yy] = 1
            if ladder[xx][yy] == 2:
                print(i)
                sys.exit()
            break  # 왼, 오, 아래 순으로 체크해서 1이 나오면 바로 브레이크
    # for문에서 왼, 오, 아래 모두 1이 없는 경우에는 이런식으로 작성X
    # 사다리타기이기 때문에 무조건 3 방향 중 하나가 1로 나오므로 for문 밖에 DFS()를 넣음
    DFS(xx, yy)


if __name__ == "__main__":
    goal = 2
    ladder = [list(map(int, input().split())) for _ in range(10)]
    for i in range(10):
        check = [[0] * 10 for _ in range(10)]
        if ladder[0][i] == 1:
            DFS(0, i)
