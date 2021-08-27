import sys

# 동전교환 (냅색 알고리즘)

sys.stdin = open("input.txt", 'r')

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())  # 거슬러 줄 금액

    # 초기화를 가장 큰 값으로 초기화해놓고 시작해야 함
    dy = [1000] * (m + 1)
    dy[0] = 0

    for i in arr:
        for j in range(i, m + 1):
            dy[j] = min(dy[j], dy[j - i] + 1)

    print(dy)
    print(dy[m])
