import sys

# 동전 바꿔주기(DFS)

# sys.stdin = open("input.txt", 'r')


def DFS(L, total):
    global cnt

    if total > t:
        return
    if L == k:
        if total == t:
            cnt += 1

    else:
        for i in range(w[L][1] + 1):
            DFS(L + 1, total + (w[L][0] * i))


if __name__ == "__main__":
    t = int(input())
    k = int(input())
    # 동전의 [금액, 개수]
    cnt = 0
    w = [list(map(int, input().split())) for _ in range(k)]
    DFS(0, 0)
    print(cnt)
