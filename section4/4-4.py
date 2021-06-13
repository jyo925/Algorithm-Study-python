import sys

# 마구간 정하기(결정알고리즘)
# 이분검색: 범위를 줄여 나가며 탐색 logN
sys.stdin = open("input.txt", 'r')


def count(distance):
    cnt = 1
    ep = x[0] #마지막으로 말이 배치된 지점

    for i in range(1, n):
        if x[i] - ep >= distance:
            cnt += 1
            ep = x[i]
    return cnt


n, m = map(int, input().split())
x = [int(input()) for _ in range(n)]
x.sort()

lt = 1
rt = x[n - 1]
res = 0

while lt <= rt:
    mid = (lt + rt) // 2
    if count(mid) >= m:
        res = mid
        lt = mid + 1 #더 큰거리를 찾도록
    else:
        rt = mid - 1

print(res)
