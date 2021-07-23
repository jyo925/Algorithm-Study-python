import sys
import itertools as it

# 수열(P) 추측하기
# 라이브러리 이용 -> 사용은 하지 말것
# 기본은 재귀를 사용해서 직접 만들어야 함
sys.stdin = open("input.txt", 'r')

n, f = map(int, input().split())
b = [1] * n

# 이항계수 계산
for i in range(1, n):
    b[i] = b[i - 1] * (n - i) // i

a = list(range(1, n + 1))
# 4개중 3개를 뽑는 순열
# for tmp in it.permutations(a, 3):
#     print(tmp)

# 4개중 3개를 뽑는 순열
for tmp in it.permutations(a):
    sum = 0
    # 위치에 따라서 이항계수 값이 다르므로 인덱스 i 필요
    for i, x in enumerate(tmp):
        sum += (x * b[i])
    if sum == f:
        for x in tmp:
            print(x, end=' ')
        break
