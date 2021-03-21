import sys

sys.stdin = open("input.txt", "rt")

n = input()
nums = list(map(int, input().split()))


# def digit_sum(x):
#     sum = 0
#     for i in str(x):
#         sum += int(i)
#     return sum

def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum

max_sum = 0
max_num = 0
for num in nums:
    num_sum = digit_sum(num)
    if num_sum > max_sum:
        max_sum = num_sum
        max_num = num

print(max_num)

