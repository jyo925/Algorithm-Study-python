# 삽입 정렬
# 정렬된 데이터에 효과적, 이 경우 퀵정렬 보다 빠름 O(n)
# 데이터를 하나씩 확인하고 적절한 위치에 삽입
# 선택 정렬에 비해 효율적
# 첫번째 데이터는 정렬되었다는 가정 하에 두번째부터 시작

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:  # 자신보다 작은 데이터를 만나면 멈춤
            break

print(array)