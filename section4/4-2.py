import sys

# 이분검색: 범위를 줄여 나가며 탐색 logN
sys.stdin = open("input.txt", 'r')


# 랜선의 길이를 입력받아서 몇개의 랜선을 만들 수 있는지 체크
def count(len):
    cnt = 0
    for x in line:
        cnt += (x // len)
    return cnt


k, n = map(int, input().split())
line = [int(input()) for i in range(k)]
res = 0

largest = max(line)

lt = 1
rt = largest

while lt <= rt:
    mid = (lt + rt) // 2
    if count(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
