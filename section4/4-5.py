import sys

# 회의실 배정(그리디)
# 그리디: 최선의 해를 구하기
sys.stdin = open("input.txt", 'r')

n = int(input())
meeting = [tuple(map(int, input().split())) for _ in range(n)]

meeting.sort(key=lambda x: (x[1], x[0]))

et = 0
cnt = 0
for s, e in meeting:
    if s >= et:
        et = e
        cnt += 1

print(cnt)
