import sys

sys.stdin = open("input.txt", 'r')

n1 = int(input())
list1 = list(map(int, input().split()))

n2 = int(input())
list2 = list(map(int, input().split()))

# merge_list = list1+list2
# merge_list.sort()

# 이미 정렬되어있는 데이터를 nlogn인 sort를 이용하는 것은 비추
# 0(n)으로 되게끔 구현하기

p1 = p2 = 0
i = 0
c = []

while p1 < n1 and p2 < n2:
    if list1[p1] <= list2[p2]:
        c.append(list1[p1])
        p1 += 1
    else:
        c.append(list2[p2])
        p2 += 1

if p1 < n1:
    c = c + list1[p1:]
if p2 < n2:
    c = c + list2[p2:]

for x in c:
    print(x, end=' ')