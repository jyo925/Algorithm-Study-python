import sys

sys.stdin = open("input.txt", "rt")


# 이진탐색(반복문 ver)
# 반으로 쪼개면서 탐색하기
# 시작점, 중간점, 끝점 활용
# 데이터가 정렬되어 있어야 함
# O(logN)
def binary_search(a, t, start, end):
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == t:
            return mid
        elif a[mid] > t:
            end = mid - 1
        else:
            start = mid + 1
    return None


n, target = list(map(int, input().split()))
a = list(map(int, input().split()))

result = binary_search(a, target, 0, n - 1)
if result is None:
    print("찾고자 하는 원소가 존재하지 않습니다.")
else:
    print(result + 1, "번째에 위치합니다.")
