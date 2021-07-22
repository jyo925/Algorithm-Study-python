import sys
import datetime
start_time = datetime.datetime.now()
# 수열 추측하기
# 핵심 시간 단축 -> 파스칼 삼각형 구할 때 연산 규칙 파악 이항계수
# 복습하기
sys.stdin = open("input.txt", 'r')


def DFS(L, s):
    if L == n and s == f:
        for x in p:
            print(x, end=' ')
        print(datetime.datetime.now() - start_time)
        sys.exit(0)
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                p[L] = i
                DFS(L + 1, s + (p[L] * b[L]))
                ch[i] = 0


if __name__ == "__main__":
    n, f = map(int, input().split())
    p = [0] * n
    b = [1] * n
    ch = [0] * (n + 1)
    for i in range(1, n):
        b[i] = b[i - 1] * (n - i) // i
    DFS(0, 0)
