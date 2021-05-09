# 퀵 정렬
# 기준데이터(피벗)를 설정하고 그 기준보다 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작
# 전통적인 방식과 다른 호어분할로 구현
# 리스트의 첫 번째 데이터를 피벗으로
# 데이터들을 항상 절반씩 쪼갠다고 가정하면 O(NlogN) 복잡도를 가지며, 최악의 경우는 O(N^2)
# 가장 왼쪽 데이터를 피벗으로 삼고 정렬된 데이터가 들어오면 O(N^2)에 가까움


array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(a, start, end):
    if start >= end:  # 원소가 1개인 경우 종료
        return
    pivot = start  # 첫번째 원소가 피벗
    left = start + 1
    right = end
    while left <= right:
        # 왼쪽에서부터 피벗보다 큰 데이터 찾기
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 오른쪽에서부터 피벗보다 작은 데이터 찾기
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # 엇갈린 경우 작은 데이터와 피벗 교체(분할)
        if left > right:
            array[right], array[pivot] = array[pivot], array[right],
        # 엇갈리지 않은 경우 작은 데이터와 큰 데이터 교체
        else:
            array[left], array[right] = array[right], array[left]

        # 분할 이후 오른쪽, 왼쪽에서 각각 퀵정렬 수행
        quick_sort(array, start, right - 1)
        quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)


def quick_sort2(a):
    if len(a) <= 1:
        return a

    pivot = a[0]
    tail = a[1:]  # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)


print(quick_sort2(array))
