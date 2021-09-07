# ** 슬라이딩 윈도우란?
#     - window를 한 칸 옮기는 (w-1)칸은 겹친다.
#     - a b c d가 있을 때
#         a b c 의 합 = s
#         b c d 의 합 = s - a + d 로 구할 수 있다. a와 d 값만 이용하면 됨 ---> o(1)
#         즉, 중복되는 값 b, c를 계산하지 않아도 됨
#         기존에는 모든 위치마다 합을 구해서 o(nm)이 걸리지만, 슬라이딩 윈도우를 사용하여 o(n)으로 해결

def solve_max_sum(arr, k):
    max_sum = float('-inf')
    start = 0
    curr_sum = 0

    for end, val in enumerate(arr):
        curr_sum += val
        if end - start + 1 == k:
            max_sum = max(max_sum, curr_sum)
            curr_sum -= arr[start]
            start += 1
    return max_sum


arr = [2, 3, 4, 1, 5]
k = 3

print(solve_max_sum(arr, k))
