# 947. Most Stones Removed with Same Row or Column
import collections
from typing import List


# print(-2 % 5) 결과가...3임!
# 원리 이해 필요


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        l = len(A)
        ht = collections.defaultdict(int)
        ht[0] = 1
        s = 0
        count = 0
        for i in range(l):
            s += A[i]
            if K:
                s = s % K

            if s in ht:
                count += ht[s]

            ht[s] += 1

        return count


print(Solution.subarraysDivByK('', [4, 5, 0, -2, -3, 1], 5))
# print(Solution.subarraysDivByK('', [5], 9))
# print(Solution.subarraysDivByK('', [-5], 5))
# print(Solution.subarraysDivByK('', [0, -5], 10))
print(-2 % 5)
