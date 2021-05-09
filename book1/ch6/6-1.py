# 선택정렬
# n-1번 가장 작은 값을 찾아서 맨 앞으로 보내기
# O(n^2)
# 매우 비효율, but 코테에서 가장 작은 데이터를 찾는 일이 있음

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)-1):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)