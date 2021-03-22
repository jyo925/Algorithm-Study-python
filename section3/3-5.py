import sys

sys.stdin = open("input.txt", 'r')

# n, m = map(int, input().split())
# nums = list(map(int, input().split()))
# # 내가 짠 코드는 입력값 많으면 시간초과남
# count = 0
# for i in range(n):
#     tmp = nums[i]
#     for j in range(i+1, n):
#         tmp += nums[j] 
#         if tmp > m:
#             break
#         elif tmp == m:
#             count += 1
#             break
#
# print(count)

# 투 포인터 lt, rt를 이용 -> 어떤 연속적인 값의 합을 구할때..
n, m = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = 1
tot = a[0]
cnt = 0

while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else:  # tot이 작지만 더이상 더할 자료가 없는 경우에 rt가 n이랑 같으면 안됨, base case
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else: # tot > m
        tot -= a[lt]
        lt += 1

print(cnt)