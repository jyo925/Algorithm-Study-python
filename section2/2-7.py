import sys

# 소수 개수 출력
# 에라토스테네스 체
# 2부터 시작, 2와 2의 배수 모두 1로 체크
# 0일 때만 +1
sys.stdin = open("input.txt", "rt")
n = int(input())

ch = [0] * (n + 1)
cnt = 0

# 이중 포문이지만 시간초과가 걸리지 않도록 구현

for i in range(2, n + 1):
    if ch[i] == 0:
        cnt += 1
        # i의 배수만 반복 체크
        for j in range(i, n + 1, i):
            ch[j] = 1

print(cnt)
