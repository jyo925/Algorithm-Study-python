import sys

# 증가수열
# sys.stdin = open("input.txt", 'r')

n = int(input())
s = list(map(int, input().split()))

res = [0]
res_s = []

while len(s) != 0:
    ll = s[0]
    r = s[-1]

    if ll > max(res) and r > max(res):
        if ll < r:
            res_s.append("L")
            res.append(ll)
            s.remove(ll)
        elif ll >= r:
            res_s.append("R")
            res.append(r)
            s.remove(r)

    elif ll > max(res) or r < max(res):
        if ll > max(res):
            res_s.append("L")
            res.append(s[0])
            s.remove(s[0])
    elif ll < max(res) or r > max(res):
        if r > max(res):
            res_s.append("R")
            res.append(r)
            s.remove(r)

    if s[0] < max(res) and s[-1] < max(res):
        break

print(len(res) - 1)
print(''.join(res_s))
