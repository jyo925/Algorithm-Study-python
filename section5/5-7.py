import sys
from collections import deque

# 교육과정 설계
# 큐 이용
sys.stdin = open("input.txt", 'r')

need = input()
n = int(input())

for i in range(n):
    plan = input()
    q = deque(need)
    for x in plan:
        if x in q:
            if x != q.popleft():
                print("#%d NO" %(i+1))
                break
    else:
        if len(q) == 0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" % (i + 1))
