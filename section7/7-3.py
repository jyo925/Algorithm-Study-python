import sys

# 양팔저울(DFS)

sys.stdin = open("input.txt", 'r')


def DFS(L, total):
    if L == k:
        # 상태트리가 대칭으로 나타나기 때문에 음수는 고려하지 X
        if 0 < total <= s:
            res.add(total)
    else:
        # L번째 추를
        DFS(L + 1, total + w[L])  # 왼쪽에 놓는 경우
        DFS(L + 1, total - w[L])  # 오른쪽에 놓는 경우
        DFS(L + 1, total)  # 놓지 않는 경우


if __name__ == "__main__":
    k = int(input())
    w = list(map(int, input().split()))
    # print(w)
    s = sum(w)
    res = set()
    DFS(0, 0)
    print(s - len(res))
