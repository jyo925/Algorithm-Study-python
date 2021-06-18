import sys

# 순열 구하기
# sys.stdin = open("input.txt", 'r')


def DFS(L):
    global cnt
    if L == m:
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):
            if ch[i] == 1:
                continue
            res[L] = i
            ch[i] = 1
            DFS(L + 1)
            ch[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    ch = [0] * (n + 1)
    cnt = 0
    DFS(0)
    print(cnt)