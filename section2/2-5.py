import sys

sys.stdin = open("input.txt", "rt")

# 4, 6, 8, 12, 20 중 하나여야 함
n, m = map(int, input().split())

n_list = [i + 1 for i in range(n)]
m_list = [i + 1 for i in range(m)]

res = []
for i in n_list:
    for k in m_list:
        res.append(i + k)

a = []
for i in set(res):
    a.append((i, res.count(i)))

a.sort(key=lambda x: -x[1])
per = a[0][1]

for i in a:
    if i[1] == per:
        print(i[0], end=' ')
