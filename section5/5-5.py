import sys
from collections import deque

# 공주 구하기
# 큐 이용
sys.stdin = open("input.txt", 'r')

n, k = map(int, input().split())
q = deque(range(1, n+1))

cnt = 0
while len(q) > 1:
    tmp = q.popleft()
    cnt += 1
    if cnt == k:
        cnt = 0
        continue
    q.append(tmp)

print(q[0])

