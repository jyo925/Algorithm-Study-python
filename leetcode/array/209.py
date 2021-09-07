# 209. Minimum Size Subarray Sum
# 문제 이해 잘못함
# is greater than or equal to target.
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        res = 21470000
        start = 0
        tmp = 0

        for i, v in enumerate(nums):
            # print(tmp, i)
            tmp += v
            while tmp >= target:
                res = min(res, i - start + 1)
                tmp -= nums[start]
                start += 1

        #     return res if res != 21470000 else 0
        if res == 21470000:
            res = 0
        return res


print(Solution.minSubArrayLen('', 7, [2, 3, 1, 2, 4, 3]))
print(Solution.minSubArrayLen('', 11, [1, 1, 1, 1, 1, 1, 1, 1]))
print(Solution.minSubArrayLen('', 4, [1, 4, 4]))
print(Solution.minSubArrayLen('', 11, [1, 2, 3, 4, 5]))
print(Solution.minSubArrayLen('', 15, [1, 2, 3, 4, 5]))
