import sys
from collections import deque

# 응급실
# 큐 이용
sys.stdin = open("input.txt", 'r')

n, m = map(int, input().split())
q = [(idx, val) for idx, val in enumerate(list(map(int, input().split())))]
q = deque(q)

cnt = 0
while True:
    cur = q.popleft()
    # 여기서 시간 복잡도가 o(n)이지 않나
    if any(cur[1] < x[1] for x in q):
        q.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            break

print(cnt)

