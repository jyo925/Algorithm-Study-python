class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []

        def dfs(elements, start):
            result.append(elements[:])
            for i in range(start, len(nums)):
                dfs(elements + [nums[i]], i + 1)

        dfs([], 0)
        return result

# class Solution:
#     def subsets(self, nums: list[int]) -> list[list[int]]:
#         result = [[]]
#
#         def dfs(elements, start, cnt):
#
#             if cnt == len(nums):
#                 # result.append(elements[:])
#                 return
#
#             else:
#
#                 for i in range(start, len(nums)):
#                     elements.append(nums[i])
#                     result.append(elements[:])
#                     dfs(elements, i + 1, cnt + 1)
#                     elements.pop()
#
#         dfs([], 0, 0)
#         return result

print(Solution.subsets("", [1, 2, 3]))
