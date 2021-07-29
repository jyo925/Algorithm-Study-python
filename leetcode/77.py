class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []

        def dfs(elements, start, cnt):

            if cnt == k:
                result.append(elements[:])
                return
            else:

                for i in range(start, n + 1):
                    elements.append(i)
                    dfs(elements, i + 1, cnt + 1)
                    elements.pop()

        dfs([], 1, 0)
        return result


print(Solution.combine("", 4, 2))
