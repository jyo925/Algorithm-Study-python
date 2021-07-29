# 내 풀이
class Solution(object):
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        res = [0] * (len(nums))
        ch = [0] * (len(nums))

        def dfs(L):
            if L == len(nums):
                result.append(res[:])
                return
            else:
                for i in range(len(nums)):
                    if ch[i] == 1:
                        continue
                    res[L] = nums[i]
                    ch[i] = 1
                    dfs(L + 1)
                    ch[i] = 0

        dfs(0)
        return result


print(Solution.permute("", [1, 2, 3]))


class Solution2(object):
    def permute(self, nums: list[int]) -> list[list[int]]:
        result =[]
        prev_elements = []

        def dfs(elements):
            if len(elements) == 0:
                result.append(prev_elements[:])

            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return result


print(Solution2.permute("", [1, 2, 3]))
