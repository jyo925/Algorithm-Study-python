import collections
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

        counts = collections.defaultdict(int)
        for word in words:
            counts[word] += 1

        res = collections.Counter(words)
        return res.most_common(1)[0][0]


print(Solution.mostCommonWord("", "Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
