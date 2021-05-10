# 7-5 문제를 집합 자료형을 이용

n = int(input())

array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array: #set 자료형은 in 연산 제공
        print('yes', end=' ')
    else:
        print('no', end=' ')