import sys

# 가방문제(냅색 알고리즘)

sys.stdin = open("input.txt", 'r')

if __name__ == "__main__":
    n, m = map(int, input().split())
    dy = [0] * (m + 1)
    # dy[j]는 j무게까지 가방에 담을 수 있을 때 보석의 최대 가치를 의미

    for i in range(n):
        w, v = map(int, input().split())
        # 핵심
        for j in range(w, m + 1):
            dy[j] = max(dy[j], dy[j - w] + v)

    print(dy[m])
