# 724. Find Pivot Index
# 슬라이딩 사용
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:

        right_sum = sum(nums)
        left_sum = 0
        last_pivot = 0
        for i in range(len(nums)):

            right_sum -= nums[i]
            left_sum += last_pivot
            last_pivot = nums[i]

            if right_sum == left_sum:
                return i

        return -1


print(Solution.pivotIndex('', [1, 7, 3, 6, 5, 6]))
# print(Solution.pivotIndex('', [1, 2, 3]))
