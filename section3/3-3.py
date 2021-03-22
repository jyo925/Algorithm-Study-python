import sys

sys.stdin = open("input.txt", 'r')

# input_range = []
# for _ in range(10):
#     input_range.append(tuple(map(int, input().split())))
#
# card = [i for i in range(1, 21)]
#
# for a, b in input_range:
#     mid = (b - a + 1) // 2
#     for _ in range(mid):
#         card[a-1], card[b-1] = card[b-1], card[a-1]
#         a += 1
#         b -= 1
#
# for i in card:
#     print(i, end=' ')

# 각각의 구간을 입력받음과 동시에 바로 swqp처리도 하면 더 간결
a = list(range(21))

for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e - s + 1) // 2):
       a[s+i], a[e-i] = a[e-i], a[s+i],

for x in a[1: ]:
    print(x, end=' ')