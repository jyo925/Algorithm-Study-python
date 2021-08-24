import sys

# 피자 배달 거리(DFS)
# 조합을 DFS로 이용

sys.stdin = open("input.txt", 'r')


def DFS(L, s):
    global res

    if L == m:
        dis_sum = 0
        for j in range(len(home)):
            x1 = home[j][0]
            y1 = home[j][1]

            # 각 집의 피자 배달 거리 구하기
            dis = 214700000
            for x in p:
                x2 = pizza[x][0]
                y2 = pizza[x][1]
                dis = min(dis, abs(x1 - x2) + abs(y1 - y2))

            dis_sum += dis
        if dis_sum < res:
            res = dis_sum

    else:
        for k in range(s, len(pizza)):
            p[L] = k
            DFS(L + 1, k + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    pz_map = [list(map(int, input().split())) for _ in range(n)]
    res = 214700000
    home = []
    pizza = []
    p = [0] * m  # 조합의 경우를 저장
    for i in range(n):
        for j in range(n):
            if pz_map[i][j] == 1:
                home.append((i, j))
            elif pz_map[i][j] == 2:
                pizza.append((i, j))

    DFS(0, 0)
    print(res)
