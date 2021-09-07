# 56. Merge Intervals
# o(nlogn)으로 풀기
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])
        res = []

        start = intervals[0][0]
        end = intervals[0][1]

        for s, e in intervals[1:]:
            # print(s, e, start, end)
            if s <= end:
                end = max(end, e)
            else:
                res.append([start, end])
                start = s
                end = e

        res.append([start, end])
        return res


print(Solution.merge('', [[1, 3], [2, 6], [8, 10], [15, 18]]))  # [[1,6],[8,10],[15,18]]
print(Solution.merge('', [[1, 4], [4, 5]]))  # [[1,5]]
