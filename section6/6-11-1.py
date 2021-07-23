import sys

# 수들의 조합
# 조합의 합이 M의 배수인게 몇 개인가?
sys.stdin = open("input.txt", 'r')


def DFS(L, s, total):
    global cnt
    if L == k:
        if total % m == 0:
            cnt += 1
    else:
        for j in range(s, n):
            res[L] = a[j]
            DFS(L + 1, j + 1, total + a[j])


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    m = int(input())
    res = [0] * k
    cnt = 0
    DFS(0, 0, 0)
    print(cnt)
