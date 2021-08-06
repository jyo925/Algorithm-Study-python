import sys

# 동전 바꿔주기(DFS)
# 동전 종류별로 개수가 다르다. 어떻게 상태트리를 그릴까?
# L은 동전 종류를 가리키고, 동전의 개수만큼 DFS 수행(0개, 1개, 2개,,,를 사용하는 경우)
# sys.stdin = open("input.txt", 'r')


def DFS(L, total):
    global cnt

    if total > t:
        return
    if L == k:
        if total == t:
            cnt += 1

    else:
        # 0~동전개수 만큼 가지 생성
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
