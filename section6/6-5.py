import sys

# 바둑이 승차(DFS)
# sys.stdin = open("input.txt", 'r')


# L은 인덱스, s는 sum, ts는 포함 여부를 떠나서 현재까지 판단한 바둑이 무게의 합
# total - tsum 값이 결국 나머지 판단해야할 바둑이 무게의 총합
# 시간 복잡도 개선을 위해 도입, 즉 판단하지 않은 바둑이 무게를 다 합해도 result 보다 값이 작으면 볼 필요가 X
def DFS(L, s, ts):
    global result
    if s + (total - ts) < result:
        return
    if s > c:
        return
    if L == n:  # 종착점이면
        if result < s:
            result = s
    else:
        DFS(L + 1, s + w[L], ts + w[L])
        DFS(L + 1, s, ts + w[L])


if __name__ == "__main__":
    c, n = map(int, input().split())
    w = [0] * n
    result = -2147000000

    for i in range(n):
        w[i] = int(input())

    total = sum(w)
    DFS(0, 0, 0)

print(result)
