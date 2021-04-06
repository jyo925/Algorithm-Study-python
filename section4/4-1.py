import sys

# 이분검색: 범위를 줄여 나가며 탐색 logN
sys.stdin = open("input.txt", 'r')

n, m = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
# print(data.index(m)+1)

# 이분검색으로 풀기
# lt, rt, mid를 이용
lt = 0
rt = n - 1
while lt <= rt:
    mid = (lt + rt) // 2
    if data[mid] == m:
        print(mid+1)
        break
    elif data[mid] > m:
        rt = mid-1
    else:
        lt = mid+1
