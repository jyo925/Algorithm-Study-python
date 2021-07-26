import sys

# 최대점수 구하기(DFS)
# n개수 m시간
# sys.stdin = open("input.txt", 'r')


# 최대 O(2^n)
def DFS(L, score, time):
    global res

    if time > m:
        return
    if L == n:
        if score > res:
            res = score
    else:
        DFS(L + 1, score + g[L][0], time + g[L][1])
        DFS(L + 1, score, time)


# 문제1 틀림, 문제1 시간초과 나옴
# 내가 푼 방법 상태트리가 다름 O(n^n) 인듯 루트가 중복이 있음
# 순열이 아닌 조합이면 됨
def DFS2(L, score, time):
    global res
    if time > m:
        return
    if L == n:
        if score > res:
            res = score
    else:
        for j in range(L, n):
            DFS(L + 1, score + g[L][0], time + g[L][1])


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(n)]
    res = -2147000000
    DFS2(0, 0, 0)
    print(res)
