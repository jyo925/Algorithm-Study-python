import sys
# 봉우리
# 전략:
# sys.stdin = open("input.txt", 'r')

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

data.insert(0, [0] * n)
data.append([0] * n)
for i in data:
    i.insert(0, 0)
    i.append(0)

d = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def check(x, y):
    for k in d:
        if data[x][y] <= data[x + k[0]][y + k[1]]:
            return False
    return True


cnt = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if check(i, j):
            cnt += 1

print(cnt)

# 다른 풀이
# all(iterable) 함수는 인자로 받은 반복 가능한 자료형(iterable)의 모든 요소가 참(True)인지 체크
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if all(data[i][j] > data[i + k[0]][j + k[1]] for k in range(4)):
#             cnt += 1
