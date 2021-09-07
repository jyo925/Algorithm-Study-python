# 162. Find Peak Element
# You must write an algorithm that runs in O(log n) time.

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:

        l = 0
        r = len(nums) - 1

        if len(nums) == 1:
            return 0

        while l < r:
            pivot = (l + r) // 2
            num1 = nums[pivot]
            num2 = nums[pivot + 1]
            if num1 < num2:
                l = pivot + 1
            else:
                r = pivot

        return r


print(Solution.findPeakElement('', [1, 2, 3, 1]))
print(Solution.findPeakElement('', [1, 2, 1, 3, 5, 6, 4]))
print(Solution.findPeakElement('', [1, 3, 2, 4, 5, 6, 8]))
