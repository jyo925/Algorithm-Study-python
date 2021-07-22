import sys
import datetime

start_time = datetime.datetime.now()
# 조합 구하기
# 중요
# s: 몇 번째부터 가지가 나가야 하는지 알려주는 숫자
# D(0)에서 0에서 나가는 가지는 1 2 3...n 까지
# D(1)에서 1에서 나가는 가지는 2 3 4 ...n
# D(1)에서 2에서 나가는 가지는 3 4 ...n
# D(1)에서 4에서 나가는 가지는 5 ...n -> n < 5 이므로 반복문 실행 X
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
            DFS(L + 1, j + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    cnt = 0
    DFS(0, 1)
    print(cnt)
