import sys

# sys.stdin = open("input.txt", 'r')
n = int(input())
test = []

for _ in range(n):
    test.append(input())

# 내가 푼 방법
for i in enumerate(test):
    for k in range(len(i[1]) // 2):
        if i[1][k].lower() != i[1][-(k + 1)].lower():
            print("#", i[0] + 1, "NO")
            break
    else:
        print("#", i[0] + 1, "YES")


# 다른 방법
for i in range(n):
    s = test[i].upper()
    if s == s[::-1]:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" % (i + 1))
