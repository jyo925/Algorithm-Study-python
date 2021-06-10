# 개미 전사(식량 창고)
# Ai번째 최대 식량은 max(Ai-1, Ai-2 + Ki)
# 보텀업

n = int(input())
food = list(map(int, input().split()))

d = [0] * 100

d[0] = food[0]
d[1] = max(food[0], food[1])

for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + food[i])

print(d[n - 1])

for i in d:
    print(i, end=' ')