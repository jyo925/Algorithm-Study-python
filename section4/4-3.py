import sys

# 뮤직비디오(결정알고리즘)
# 이분검색: 범위를 줄여 나가며 탐색 logN
sys.stdin = open("input.txt", 'r')


# DVD 몇 장 필요한지 반환하는 함수
def count(capacity):
    cnt = 1
    sum_capacity = 0
    for x in music:
        if sum_capacity + x > capacity:
            cnt += 1
            sum_capacity = x
        else:
            sum_capacity += x
    return cnt


n, m = map(int, input().split())
music = list(map(int, input().split()))


lt = 1
rt = sum(music)
max_music = max(music)
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if mid >= max_music and count(mid) <= m:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(res)
