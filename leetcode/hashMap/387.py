# 387. First Unique Character in a String
# o(2n) -> o(n), o(26) -> o(1)
# 해쉬맵 사용


class Solution:
    def firstUniqChar(self, s: str) -> int:

        ch = {}
        for i in s:
            if ch.get(i) is None:
                ch[i] = 1
            else:
                ch[i] += 1
        # python 딕셔너리는 순서보장이 되는것으로 바뀌어서 굳이 필요 없
        for j in range(len(s)):
            if ch[s[j]] == 1:
                return j

        return -1


print(Solution.firstUniqChar("", "leetcode"))
