import sys

# 수들의 조합
# 조합의 합이 M의 배수인게 몇 개인가?
# 내 풀이
# for문 내는 아니지만 sum() 시간복잡도는 o(n)임
sys.stdin = open("input.txt", 'r')


def DFS(L, s):
    global cnt
    if L == k:
        if sum(res) % m == 0:
            cnt += 1
    else:
        for j in range(s, n): # 0 ~ n - 1
            res[L] = a[j]
            DFS(L + 1, j + 1)


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    m = int(input())
    res = [0] * k
    cnt = 0
    DFS(0, 0)
    print(cnt)
