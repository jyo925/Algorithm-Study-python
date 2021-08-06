import sys

# 동전 분배하기(DFS)
# 3명에게 총 합이 다르게 동전을 어떻게 분배할지?

sys.stdin = open("input.txt", 'r')


def DFS(L):
    global res

    #마지막 동전까지 분배했다면
    if L == n:
        tmp = set(money)
        cha = max(tmp) - min(tmp)
        if len(tmp) == 3 and cha < res:
            res = cha
        return
    else:
        # 3명
        for i in range(3):
            money[i] += coin[L]
            DFS(L + 1)
            money[i] -= coin[L]


if __name__ == "__main__":
    n = int(input())
    coin = [int(input()) for _ in range(n)]
    res = 21470000
    # A,B,C 사람의 금액
    money = [0] * 3
    DFS(0)
    print(res)
