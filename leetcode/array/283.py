class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero] = nums[i]
                zero += 1

        for k in range(zero, len(nums)):
            nums[k] = 0

        print(nums)


print(Solution.moveZeroes('', [0, 1, 0, 3, 12]))
print(Solution.moveZeroes('', [1]))
