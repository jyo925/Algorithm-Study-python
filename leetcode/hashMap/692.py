# 692. Top K Frequent Words
# o(nlogn), o(n)
# o(nlogk)로 변경하려면? -> 해쉬맵에서 힙을 사용

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:

        ch = {}
        for i in range(len(words)):

            if ch.get(words[i]):
                ch[words[i]] += 1
            else:
                ch[words[i]] = 1

        # sorted는 o(nlogn)
        tmp = sorted(ch.items(), key=lambda x: (-x[1], x[0]))

        return [tmp[i][0] for i in range(k)]


print(Solution.topKFrequent("", ["i", "love", "leetcode", "i", "love", "coding"], 3))
print(Solution.topKFrequent("", ["i", "love", "leetcode", "i", "love", "coding"], 2))
