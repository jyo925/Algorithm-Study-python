import sys

# 증가수열
sys.stdin = open("input.txt", 'r')

n = int(input())
s = list(map(int, input().split()))

res = [0]
res_s = []

while len(s) != 0:
    lt = s[0]
    rt = s[-1]

    if lt > max(res) and rt > max(res):
        if lt < rt:
            res_s.append("L")
            res.append(lt)
            s.remove(lt)
        elif lt >= rt:
            res_s.append("R")
            res.append(rt)
            s.remove(rt)

    elif lt > max(res) or rt < max(res):
        if lt > max(res):
            res_s.append("L")
            res.append(s[0])
            s.remove(s[0])
    elif lt < max(res) or rt > max(res):
        if rt > max(res):
            res_s.append("R")
            res.append(rt)
            s.remove(rt)

    if s[0] < max(res) and s[-1] < max(res):
        break

print(len(res) - 1)
print(''.join(res_s))

