import sys

# 계단오르기(탑다운)

sys.stdin = open("input.txt", 'r')


def DFS(x):
    if dy[x] > 0:
        return dy[x]
    if x == 1 or x == 2:
        return x
    else:
        dy[x] = DFS(x-1) + DFS(x-2)
        return dy[x]


if __name__ == "__main__":
    n = int(input())
    dy = [0] * (n + 1)
    print(DFS(n))
