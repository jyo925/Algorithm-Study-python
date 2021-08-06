import sys

# 알파코드(DFS)
# 다른풀이
# 상태트리를 1~26 for문을 돌면서
sys.stdin = open("input.txt", 'r')


def DFS(L, P):
    global cnt

    if L == n:
        cnt += 1
        for j in range(P):
            print(chr(res[j]+64), end='')
        print()
    else:
        for i in range(1, 27):
            if code[L] == i:
                res[P] = i
                DFS(L + 1, P + 1)
            elif i >= 10 and code[L] == i // 10 and code[L + 1] == i % 10:
                res[P] = i
                DFS(L + 2, P + 1)


if __name__ == "__main__":
    code = list(map(int, input()))
    n = len(code)
    code.insert(n, -1)  # 22번라인에서 code[-1]의 값이 2인경우 인덱스 오류가 나기 때문
    res = [0] * (n + 3)
    cnt = 0
    DFS(0, 0)
    print(cnt)
