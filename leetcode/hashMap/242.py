# 242. Valid Anagram


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #         1. 정렬해서 푸는 방법 o(nlogn)
        #         s = list(s)
        #         t = list(t)
        #         s.sort()
        #         t.sort()

        #         if len(s) != len(t):
        #             return False

        #         for i in range(len(s)):
        #             if s[i] != t[i]:
        #                 return False

        #         return True

        # 2. 해시맵 이용 o(n)
        ch = {}
        for i in s:
            if ch.get(i):
                ch[i] += 1
            else:
                ch[i] = 1

        for j in t:
            if ch.get(j):
                ch[j] -= 1
            else:
                return False

        for k in s:
            if ch.get(k) != 0:
                return False
        return True


print(Solution.isAnagram("", "anagram", "nagaram"))
