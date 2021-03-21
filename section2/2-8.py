import sys

# 소수 개수 출력
# sys.stdin = open("input.txt", "rt")
n = int(input())
numbers = list(map(int, input().split()))


def reverse(x):
    res = 0
    t = 0
    while x > 0:
        t = x % 10
        res = (res * 10) + t
        x = x // 10
    return res


def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True


for i in numbers:
    revers_num = reverse(i)
    if isPrime(revers_num):
        print(revers_num, end=' ')
    # print(revers_num)
