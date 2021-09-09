# 322. Coin Change
from typing import List


# 시간을 조금 단축
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = [2147000] * amount
        n.insert(0, 0)

        for i in range(1, amount + 1):
            tmp = 21470000
            for k in coins:
                if (i - k) >= 0 and n[i - k] != -1:
                    tmp = min(n[i - k] + 1, tmp)

            if tmp != 21470000:
                n[i] = tmp
                continue
            n[i] = -1

        return n[-1]


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = [2147000] * amount
        n.insert(0, 0)

        for i in range(1, amount + 1):
            tmp = []
            for k in coins:
                if (i-k) >= 0 and n[i-k] != -1:
                    tmp.append(n[i-k] + 1)
            if len(tmp) > 0:
                n[i] = min(tmp)
            else:
                n[i] = -1

        return n[-1]


# print(Solution.coinChange('', [1, 2, 5], 11))
print(Solution.coinChange('', [2], 3))
print(Solution.coinChange('', [1], 0))
print(Solution.coinChange('', [1], 2))
