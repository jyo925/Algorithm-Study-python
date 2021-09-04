# 290. Word Pattern
# 양방향 해쉬맵 사용

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        s = s.split()
        ch1 = {}
        ch2 = {}
        if len(s) != len(pattern):
            return False
        for i in range(len(pattern)):
            if ch1.get(pattern[i]) and ch2.get(s[i]):
                if ch1[pattern[i]] != s[i] or ch2[s[i]] != pattern[i]:
                    return False
            elif ch1.get(pattern[i]) is None and ch2.get(s[i]) is None:
                ch1[pattern[i]] = s[i]
                ch2[s[i]] = pattern[i]
            else:
                return False

        return True


# print(Solution.wordPattern("", "abba", "dog cat cat dog"))
# print(Solution.wordPattern("", "abba", "dog cat cat fish"))
# print(Solution.wordPattern("", "abba", "dog dog dog dog")) # False
print(Solution.wordPattern("", "aaa", "aa aa aa aa"))



