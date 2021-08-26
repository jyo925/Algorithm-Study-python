import sys

# 네트워크 선 자르기(탑다운-재귀, 메모이제이션)

sys.stdin = open("input.txt", 'r')


def DFS(x):
    # 재귀는 연산이 너무 많아지기 때문에 메모이제이션을 사용하는 것이 중요
    if dy[x] > 0:
        return dy[x]
    # 1이나 2인 경우는 답도 1 or 2개이기 때문
    if x == 1 or x == 2:
        return x
    else:
        dy[x] = DFS(x-1) + DFS(x-2)
        return dy[x]


if __name__ == "__main__":
    n = int(input())
    dy = [0] * (n + 1)
    print(DFS(n))
