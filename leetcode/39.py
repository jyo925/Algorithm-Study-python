class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        result = []

        def dfs(elements, start, total):

            if total > target:
                return

            if total == target:
                result.append(elements[:])
                return
            else:

                for i in range(start, len(candidates)):
                    if candidates[i] != 0:
                        elements.append(candidates[i])
                        dfs(elements, i, total+candidates[i])
                        elements.pop()

        dfs([], 0, 0)
        return result


print(Solution.combinationSum("", [2,3,0,7], 7))
print(Solution.combinationSum("", [2,3,5], 8))
