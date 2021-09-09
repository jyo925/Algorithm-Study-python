# 53. Maximum Subarray
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums) * [0]
        n[0] = nums[0]

        for i in range(1, len(nums)):
            n[i] = max(n[i - 1] + nums[i], nums[i])

        return max(n)


print(Solution.maxSubArray('', [-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(Solution.maxSubArray('', [5, 4, -1, 7, 8]))