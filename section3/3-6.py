import sys
import datetime
sys.stdin = open("input.txt", 'r')

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

# # 행의 합
# row_sum = [sum(i) for i in data]
#
# # 열의 합은 ? 0열 ->
# col_sum = 0
# for i in range(n):
#     tmp = 0
#     for j in range(n):
#         tmp += data[j][i]
#     row_sum.append(tmp)
#
# # 대각선의 합
# d1 = 0
# d2 = 0
# for i in range(n):
#     d1 += data[i][i]
#     d2 += data[n - i - 1][i]
#
# row_sum.append(d1)
# row_sum.append(d2)
#
# print(max(row_sum))
start_time = datetime.datetime.now()

largest = -2147000000
# 행과 열의 합 동시에
for i in range(n):
    row_sum = col_sum = 0
    for j in range(n):
        row_sum += data[i][j]
        col_sum += data[j][i]
    if row_sum > largest:
        largest = row_sum
    if col_sum > largest:
        largest = col_sum

# # 대각선 합 구하기
d1 = d2 = 0
for i in range(n):
    d1 += data[i][i]
    d2 += data[i][n - i - 1]
    if d1 > largest:
        largest = d1
    if d2 > largest:
        largest = d2

print(largest)
print("time :", datetime.datetime.now() - start_time)
