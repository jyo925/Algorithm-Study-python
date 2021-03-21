import sys

# sys.stdin = open("input.txt", 'r')
n = int(input())
test = []

for _ in range(n):
    test.append(input())

isSame = True
for i in enumerate(test):
    for k in range(len(i[1])//2):
        if i[1][k].lower() != i[1][-(k + 1)].lower():
            isSame = False
    if not isSame:
        print("#", i[0] + 1, "NO")
    else:
        print("#", i[0] + 1, "YES")
    isSame = True