# 75. Sort Colors

class Solution:
    def sortColors(self, nums: list[int]) -> None:

        idx0 = 0
        idx2 = len(nums) - 1
        i = 0

        while i <= idx2:

            if nums[i] == 0:
                nums[i], nums[idx0] = nums[idx0], nums[i]
                i += 1
                idx0 += 1
            elif nums[i] == 2:
                nums[i], nums[idx2] = nums[idx2], nums[i]
                idx2 -= 1
            else:
                # 1인경우
                i += 1


# print(Solution.sortColors('', [2, 0, 2, 1, 1, 0]))
print(Solution.sortColors('', [2, 0, 1]))
