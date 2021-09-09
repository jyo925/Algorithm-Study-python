from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_p = [0] * len(nums)
        max_p = [0] * len(nums)

        min_p[0], max_p[0] = nums[0], nums[0]

        for i in range(1, len(nums)):
            tmp = nums[i]
            min_p[i] = min(min_p[i - 1] * tmp, max_p[i - 1] * tmp, tmp)
            max_p[i] = max(min_p[i - 1] * tmp, max_p[i - 1] * tmp, tmp)

        return max(max_p)


# print(Solution.maxProduct("", [2, 3, -2, 4]))
# print(Solution.maxProduct("", [-2, 0, -1]))
print(Solution.maxProduct("", [-2, -3, 7]))
