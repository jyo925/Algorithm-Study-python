import sys

# 역수열
# 오름차순
# 이미 자리잡은 숫자는 나보다 작은 숫자라는 것
sys.stdin = open("input.txt", 'r')

n = int(input())
a = list(map(int, input().split()))

seq = [0] * n

for i in range(n):
    for j in range(n):
        # a[i]==0이라는 것은 자기보다 큰 숫자들이 들어올 공간이 앞에 다 확보되었다는 것
        if a[i] == 0 and seq[j] == 0:
            seq[j] = i + 1
            break
        elif seq[j] == 0:
            a[i] -= 1

print(' '.join(map(str, seq)))
