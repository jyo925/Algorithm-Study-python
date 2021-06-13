import sys

# 증가수열
# 다른 풀이
# lt, rt를 포인터로 이용하고, 튜플과 임시 리스트를 사용하여 더 간결하게 개선
sys.stdin = open("input.txt", 'r')

n = int(input())
a = list(map(int, input().split()))

# 수열의 최대값 기록
last = 0

lt = 0
rt = n - 1
res = ""
tmp = []

while lt <= rt:
    if a[lt] > last:
        tmp.append((a[lt], 'L'))
    if a[rt] > last:
        tmp.append((a[rt], 'R'))
    tmp.sort()
    # lt, rt 모두 last 보다 작은 경우 (종료조건)
    if len(tmp) == 0:
        break
    else:
        res = res + tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
    tmp.clear()

print(len(res))
print(res)
