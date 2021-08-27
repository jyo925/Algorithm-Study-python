import sys

# 최대점수 구하기(냅색 알고리즘) - 조건: 한 유형당 한개만 풀 수 있다.
# 2차원 대신 메모리 효율을 위해 1차원 배열 사용
# 배열 뒷쪽부터 계산해야 중복 적용이 안 됨

# sys.stdin = open("input.txt", 'r')

if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    dy = [0] * (m + 1)
    ch = [0] * n
    for i in range(n):
        for j in range(m, arr[i][1] - 1, -1):
            dy[j] = max(dy[j], dy[j - arr[i][1]] + arr[i][0])

    print(dy[-1])

