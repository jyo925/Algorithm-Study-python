import sys
import heapq as hq
# 최소힙
# 값이 삽입되면 부모와 값을 비교하여 swap, 부모보다 작을 때 까지 계속 타고 올라가는 방식(업 힙)
# 루트 값을 삭제하면 맨 끝 요소를 루트로 가져와서 두 자식중 작은 값과 비교하여 swap, 자식보다 클 때까지 반복(다운 힙)
# 파이썬 힙큐 지원
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
            print(hq.heappop(a)) # a를 힙구조로 만들어서 루트 노드를 pop
    else:
        hq.heappush(a, num)

