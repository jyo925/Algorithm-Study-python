import sys
import datetime

start_time = datetime.datetime.now()
# 중복 조합
sys.stdin = open("input.txt", 'r')


def DFS(L, s):
    global cnt
    if L == m:
        for x in res:
            print(x, end=' ')
        print()
        cnt += 1
    else:
        for j in range(s, n + 1):
            res[L] = j
            DFS(L + 1, j)


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    cnt = 0
    DFS(0, 1)
    print(cnt)
