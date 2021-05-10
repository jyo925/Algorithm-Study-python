# 떡볶이 떡 만들기
# 파라메트릭 서치(Parametric Search): 최적화 문제를 결정문제(예/아니오)로 바꾸어 해결하는 기법
# 적절한 높이를 찾을 때까지 높이를 반복해서 조정
# 높이의 범위를 좁혀 나갈 때 이진 탐색을 이용

n, m = list(map(int, input().split(' ')))
# 떡 길이
array = list(map(int, input().split()))

start = 0
end = max(array)
result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid

    # 길이가 부족한 경우 높이를 감소
    if total < m:
        end = mid - 1
    else:
        # 길이가 충분한 경우 우선 높이를 저장(최대한 짧게 잘랐을 때가 답)
        result = mid
        start = mid + 1

print(result)