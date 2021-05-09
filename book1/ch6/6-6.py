# 계수 정렬
# O(N+K), K는 데이터 중 최댓값
# 모든 범위를 담을 수 있는 리스트(배열)를 사용하며, 매우 빠름
# 단, 데이터의 크기가 한정적이고 중복된 데이터가 많은 경우 효과적

array = [7, 9, 5, 4, 7, 5, 7, 7, 8, 9, 9, 0, 3, 1, 6, 2, 4, 8]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for j in range(len(count)):
    for k in range(count[j]):
        print(j, end=' ')
