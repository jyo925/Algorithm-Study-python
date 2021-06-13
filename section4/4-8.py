import sys
from collections import deque

# 타이나틱
# 리스트는 pop(0) 맨 앞 요소를 삭제하면 모든 요소가 앞으로 한칸씩 이동해야 한다. o(n)
# 덱을 사용해볼 것 popleft() o(1)
sys.stdin = open("input.txt", 'r')

n, limit = map(int, input().split())
w = list(map(int, input().split()))
w.sort()
w = deque(w)
cnt = 0

while w:
    # 한 명만 남은 경우
    if len(w) == 1:
        cnt += 1
        break
    if w[0] + w[-1] > limit:
        w.pop()
        cnt += 1
    else:
        w.popleft()
        w.pop()
        cnt += 1

print(cnt)
