import sys

# 아나그램
# 딕셔너리 해쉬
sys.stdin = open("input.txt", 'r')

w1 = input()
w2 = input()
q1 = dict()

# for x in w1:
#     if q1.get(x):
#         q1[x] = q1[x] + 1
#     else:
#         q1[x] = 1
#
# for x in w2:
#     if q1.get(x):
#         q1[x] -= 1
#         if q1[x] == 0:
#             q1.pop(x)
#     else:
#         print("NO")
#         break
#
# if len(q1) == 0:
#     print("YES")

# q1[x] = q1[x] + 1는 잘 실행되지만 강의에서 키 에러가 난다고 해서 개선
for x in w1:
    q1[x] = q1.get(x, 0) + 1  #x라는 키 값이 있으면 값을 리턴 없으면 0을 리턴

for x in w2:
    q1[x] = q1.get(x) - 1

for x in w1:
    if q1.get(x) != 0:
        print("NO")
        break
else:
    print("YES")
