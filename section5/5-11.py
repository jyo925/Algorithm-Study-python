import sys
import heapq as hq
# 최대힙
# 부모가 두 자식보다 값이 큼
# 파이썬 힙큐는 기본이 최소힙 -> 부호만 바꿔주면 됨
sys.stdin = open("input.txt", 'r')
a = []


while True:
    num = int(input())
    if num == -1:
        break
    elif num == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(-hq.heappop(a)) # a를 힙구조로 만들어서 루트 노드를 pop
    else:
        hq.heappush(a, -num)

