import sys

# 알리바바와 40인의 도둑(Bottom-Up)
# 0행과 0열만 다이나믹 값을 초기화하고 시작

# sys.stdin = open("input.txt", 'r')

if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dy = [[0] * n for _ in range(n)]

    dy[0][0] = arr[0][0]
    for i in range(n):
        dy[0][i] = dy[0][i - 1] + arr[0][i]
        dy[i][0] = dy[i - 1][0] + arr[i][0]

    for j in range(1, n):
        for k in range(1, n):
            dy[j][k] = arr[j][k] + min(dy[j - 1][k], dy[j][k - 1])

    print(dy[n - 1][n - 1])
