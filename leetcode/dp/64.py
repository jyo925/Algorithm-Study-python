# 64. Minimum Path Sum
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        # 벽쪽 초기화 작업
        for i in range(1, len(grid[0])):
            grid[0][i] += grid[0][i - 1]

        for j in range(1, len(grid)):
            grid[j][0] += grid[j - 1][0]

        for k in range(1, len(grid)):
            for h in range(1, len(grid[k])):
                grid[k][h] += min(grid[k - 1][h], grid[k][h - 1])

        return grid[-1][-1]


# print(Solution.minPathSum('', [[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(Solution.minPathSum('', [[1, 2, 3], [4, 5, 6]]))
