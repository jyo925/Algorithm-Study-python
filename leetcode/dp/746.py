# 746. Min Cost Climbing Stairs
from typing import List


# top칸 비용을 0이라고 두고 품...ㅋㅋ
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        top = len(cost)
        k = [0] * top
        k[0] = cost[0]
        k[1] = cost[1]

        if top == 1:
            return 0

        for i in range(2, len(cost)):
            k[i] = min(k[i - 2], k[i - 1]) + cost[i]

        return min(k[-2], k[-1])


print(Solution.minCostClimbingStairs('', [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
