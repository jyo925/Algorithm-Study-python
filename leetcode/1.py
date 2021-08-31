class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_map = {}

        for i, v in enumerate(nums):
            nums_map[v] = i

        for i, v in enumerate(nums):

            if target-v in nums_map and i != nums_map[target-v]:
                return i, nums_map[target-v]

