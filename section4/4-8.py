import sys

# 타이나틱
# sys.stdin = open("input.txt", 'r')

n, m = map(int, input().split())
w = list(map(int, input().split()))

w.sort()

cnt = 0

while len(w) != 0:

    for i in w[:-1]:
        if w[-1] + i <= m:
            cnt += 1
            w.remove(w[-1])
            w.remove(i)
            break
    else:
        cnt += 1
        w.remove(w[-1])


print(cnt)
