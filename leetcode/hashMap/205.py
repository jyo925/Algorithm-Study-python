# 205. Isomorphic Strings
# o(n), o(26) -> o(1)
# 해쉬맵 사용

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False

        ch1 = {}
        ch2 = {}
        for i in range(len(s)):
            m1 = ch1.get(s[i])
            m2 = ch2.get(t[i])

            if m1 is None and m2 is None:
                ch1[s[i]] = t[i]
                ch2[t[i]] = s[i]
            else:
                if not (m1 == t[i] and m2 == s[i]):
                    return False
        return True


print(Solution.isIsomorphic("", "bacd", "baba"))


