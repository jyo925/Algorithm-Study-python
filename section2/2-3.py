import sys

sys.stdin = open("input.txt", "rt")

# n은 카드 개수, k는 k번째로 큰 수
n, k = map(int, input().split())
a = list(map(int, input().split()))  # 카드 숫자 입력

result = set()

for i in range(n):
    for j in range(i+1,n):
        for m in range(j+1, n):
            result.add(a[i]+a[j]+a[m])

result = list(result)
result.sort(reverse=True)
print(result[k-1])



