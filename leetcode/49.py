import collections


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)

        return anagrams.values()


print(Solution.groupAnagrams("", ["eat", "tea", "tan", "ate", "nat", "bat"]))
