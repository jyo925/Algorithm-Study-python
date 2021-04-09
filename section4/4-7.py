import sys

# 창고 정리
sys.stdin = open("input.txt", 'r')

x = int(input())
h = list(map(int, input().split()))
m = int(input())

# for _ in range(m):
#     min_box = min(h)
#     max_box = max(h)
#     h[h.index(min_box)] += 1
#     h[h.index(max_box)] -= 1
#
# print(max(h) - min(h))


# 다른 풀이
h.sort()
for _ in range(m):
    h[0] += 1
    h[x-1] -= 1
    h.sort()

print(h[x-1] - h[0])
