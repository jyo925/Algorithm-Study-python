import sys

sys.stdin = open("input.txt", "rt")
n = int(input())

max_money = 0

for i in range(n):
    tmp = input().split()
    tmp.sort(reverse=True)
    a, b, c = map(int, tmp)

    if a == b and b == c:
        money = 10000 + a * 1000
    elif a == b or a == c:
        money = 1000 + a * 100
    elif b == c:
        money = 1000 + b * 100
    else:
        money = a * 100

    if money > max_money:
        max_money = money

print(max_money)