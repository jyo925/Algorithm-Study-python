import sys

# 알파코드(DFS)
# 상태트리를 한자리 증가하는 경우와 두자리 증가하는 경우로 그려서 품
sys.stdin = open("input.txt", 'r')


def DFS(L, s):
    global cnt
    if L > len(n):
        return

    if L == len(n):
        w.append(s)
        cnt += 1

    else:
        c1 = int(n[L])
        c2 = int(n[L:L + 2])
        if c1 == 0:
            return
        DFS(L + 1, s[:] + chr(c1 + 64))
        if c2 > 26:
            return
        DFS(L + 2, s[:] + chr(c2 + 64))


if __name__ == "__main__":
    n = input()
    w = []
    cnt = 0
    DFS(0, "")
    w.sort()
    for i in w:
        print(i)
    print(cnt)
