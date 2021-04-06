import sys

# 회의실 배정(그리디)
# 그리디: 최선의 해를 구하기
# 리스트 내부끼리도 비교하도록 수정해야함
sys.stdin = open("input.txt", 'r')

n = int(input())
person = [tuple(map(int, input().split())) for _ in range(n)]
et = 0
x = []
for s, e in person:
    x.append((s, e))
    for x_s, x_e in x:
        if s < x_s and e < x_e:
            x.pop(-1)
            break
        elif s > x_s and e > x_e:
            x.remove((x_s, x_e))

print(len(x))
print(x)

