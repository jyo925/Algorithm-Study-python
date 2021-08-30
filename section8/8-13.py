import sys

# 회장뽑기(플로이드-워샬 응용)

# sys.stdin = open("input.txt", 'r')

if __name__ == "__main__":
    n = int(input())
    dis = [[5000] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dis[i][i] = 0
    while True:
        a, b = map(int, input().split())
        if a == -1 and b == -1:
            break
        else:
            dis[a][b] = 1
            dis[b][a] = 1

    # 플로이드 워셜 적용
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

    # 출력
    dis_min = []
    for i in dis[1:]:
        dis_min.append(max(i[1:]))

    res = min(dis_min)
    res_index = []
    for i, v in enumerate(dis_min):
        if v == res:
            res_index.append(i+1)

    print(res, len(res_index))
    for i in res_index:
        print(i, end=' ')






