# 70. Climbing Stairs
class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        k = [0] * (n + 1)
        k[1] = 1
        k[2] = 2

        for i in range(3, n+1):
            k[i] = k[i - 2] + k[i - 1]

        return k[-1]


print(Solution.climbStairs('', 3))
