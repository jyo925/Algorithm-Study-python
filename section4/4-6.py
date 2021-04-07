import sys

# 회의실 배정(그리디)
# 그리디: 최선의 해를 구하기
# 리스트 내부끼리도 비교하도록 수정해야함
# sys.stdin = open("input.txt", 'r')

n = int(input())
person = [tuple(map(int, input().split())) for _ in range(n)]
et = 0
x = []

for i in range(n):
    for h, w in person:
        if person[i][0] < h and person[i][1] < w:
            x.append((person[i][0], person[i][1]))

result = list(set(person).difference(x))
print(len(result))
