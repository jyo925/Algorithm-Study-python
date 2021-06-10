import sys

sys.stdin = open("input.txt", "rt")

n = input()
score = list(map(int, input().split()))
# round 함수는 0.500상태에서 1로 반올림 못함
# 숫자에 + 0.5를 하고 int형으로 변환하는 방법을 사용하기
avg = round(sum(score) / len(score))

result = []

# 학생번호, 학생점수, 차이값 튜플
for i in enumerate(score):
    result.append((i[0], i[1], abs(avg - i[1])))

result.sort(key=lambda x: (x[2], -x[1], x[0]))

print(avg, result[0][0] + 1)
