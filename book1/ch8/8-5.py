# 1로 만들기
# 보텀업 방식
# Ai = min(Ai-1, Ai/2, Ai/3, Ai/5) + 1의 점화식이 성립

x = int(input())

d = [0] * 30001

for i in range(2, x + 1):
    # 1을 빼는 경우
    d[i] = d[i-1] + 1
    # 2,3,5 중 나눴을 때 연산 횟수가 최소인 것으로
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])