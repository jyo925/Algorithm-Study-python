import sys
# 사과나무(다이아몬드)
# 전략: s,e를 이용해서 s는 작아지고 e는 커지는 방식으로 다이아몬드를 만들어가며 구하기
# sys.stdin = open("input.txt", 'r')

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

res = 0
# 중간지점 열 구하기
s = e = n // 2

for i in range(n):
    for j in range(s, e + 1):
        res += data[i][j]

    if i < n // 2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(res)
