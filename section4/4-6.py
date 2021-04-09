import sys

# 씨름선수
# 그리디: 최선의 해를 구하기
sys.stdin = open("input.txt", 'r')

n = int(input())
person = [tuple(map(int, input().split())) for _ in range(n)]
# x = []
#
# for i in range(n):
#     for h, w in person:
#         if person[i][0] < h and person[i][1] < w:
#             x.append((person[i][0], person[i][1]))
#
# result = list(set(person).difference(x))
# print(len(result))

# 다른 풀이
# 이중 for문은 비효율적이므로 하나로 끝내도록 개선
# 키로 정렬하고 시작
# 몸무게를 이용해 최대값이 갱신될때마다 카운팅하면 된다.

person.sort(reverse=True)
largest = 0
cnt = 0
for h, w in person:
    if w > largest:
        cnt += 1
        largest = w
print(cnt)

