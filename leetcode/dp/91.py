# 91. Decode Ways


# 이전에 비슷한 문제를 DFS로 풀었음 o(2^n)
# 그러나 재귀를 사용하기 떄문에 시간 초과 발생
# 해당 문제 조건은 1 <= s.length <= 100
# DP 방식으로 풀이
class Solution:

    # def numDecodings(self, s: str) -> int:
    #
    #     cnt = 0
    #
    #     def DFS(L, a):
    #         nonlocal cnt  # 중첩함수에서 바깥 함수의 변수를 사용하려면 global이 아닌 nonlocal 키워드 사용
    #         if L > len(s):
    #             return
    #
    #         if L == len(s):
    #             cnt += 1
    #
    #         else:
    #             c1 = int(s[L])
    #             c2 = int(s[L:L + 2])
    #             if c1 == 0:
    #                 return
    #             DFS(L + 1, a[:] + chr(c1 + 64))
    #             if c2 > 26:
    #                 return
    #             DFS(L + 2, a[:] + chr(c2 + 64))
    #
    #     DFS(0, "")
    #
    #     return cnt

    def numDecodings(self, s: str) -> int:

        if len(s) == 1 and s[0] == "0":
            return 0

        n = len(s) * [0]
        n.append(1)

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                continue

            if i == len(s) - 1:
                n[i] = 1
                continue

            s2 = int(s[i:i + 2])
            if s2 < 27:
                n[i] = n[i + 1] + n[i + 2]
            else:
                n[i] = n[i + 1]

        return n[0]


# print(Solution.numDecodings('', "212325"))
print(Solution.numDecodings('', "10"))
