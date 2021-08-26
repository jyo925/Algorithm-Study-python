import sys

# 가장 높은 탑 쌓기(LIS 응용)

sys.stdin = open("input.txt", 'r')

n = int(input())
# 넓이, 높이, 무게
bricks = [list(map(int, input().split())) for _ in range(n)]
bricks.sort(key=lambda x: (x[0], x[2]))
bricks.insert(0, [0, 0, 0])
dy = [0] * (n + 1)
dy[1] = bricks[1][1]
res = bricks[1][1]

for i in range(2, n + 1):
    max = 0
    for j in range(i - 1, 0, -1):
        if bricks[i][0] > bricks[j][0] and bricks[i][2] > bricks[j][2] and dy[j] > max:
            max = dy[j]

    dy[i] = max + bricks[i][1]
    res = max(res, dy[i])

print(res)
# print(dy)
