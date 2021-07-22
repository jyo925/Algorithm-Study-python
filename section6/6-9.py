import sys
import datetime
start_time = datetime.datetime.now()

# 수열 추측하기
# 내 풀이
sys.stdin = open("input.txt", 'r')


def check(x):
    y = []
    while True:
        if len(x) == 1:
            break
        for i in range(len(x) - 1):
            y.append(x[i] + x[i + 1])
        x = y
        y = []
    return x[0]


def DFS(L):
    if L == n:
        # for j in range(n):
        #     print(ch[j], end=' ')
        # 이때 ch 리스트에 있는 요소로 계산해야 함
        # 반환되는 계산 값이 m과 같은 경우 ch 출력 및 DFS 시스템 종료
        x = ch[:-1]
        if check(x) == m:
            for j in range(n):
                print(ch[j], end=' ')
            print(datetime.datetime.now() - start_time)
            sys.exit(0)
    else:
        for i in range(0, n):
            if ch[i] != 0:
                continue
            ch[i] = a[L]
            DFS(L + 1)
            ch[i] = 0


if __name__ == "__main__":

    n, m = map(int, input().split())
    a = [i + 1 for i in range(n)]
    ch = [0] * (n + 1)
    cnt = 0
    DFS(0)

