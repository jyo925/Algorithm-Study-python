import heapq
from typing import List


def heapSort(nums: List[int]) -> List[int]:
    nums = [-1 * n for n in nums]
    heapq.heapify(nums)
    # print(nums)

    sorted = [0] * len(nums)

    for i in range(len(nums) - 1, -1, -1):
        largest = -1 * heapq.heappop(nums)
        sorted[i] = largest
    return sorted


print(heapSort(nums=[3, 5, 9, 4, 2, 7]))
