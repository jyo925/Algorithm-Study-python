class Solution:
    # 내 풀이는 아래 풀이에 비해 공간복잡도가 좀더 쓰임
    def distance1(self, s: list):
        stack = []
        res = [0] * len(s)

        for i, v in enumerate(s):
            if len(stack) == 0:
                stack.append([i, v])
                continue
            while stack and stack[-1][1] < v:
                tmp = stack.pop()
                res[tmp[0]] = i - tmp[0]
            stack.append([i, v])

        return res

    def distance2(self, s: list):

        stack = []
        index = len(s) - 1
        for i in s[::-1]:
            if not stack:
                s[index] = 0
                stack.append([i, index])
                index -= 1
                continue

            if i > stack[-1][0]:
                while stack and i > stack[-1][0]:
                    stack.pop()
                if not stack:
                    s[index] = 0
                else:
                    s[index] = stack[-1][1] - index

            elif i < stack[-1][0]:
                s[index] = stack[-1][1] - index

            stack.append([i, index])
            index -= 1

        return s


# 답 2,1,4,2,1,1,0,0
print(Solution.distance2('', [39, 20, 70, 36, 30, 60, 80, 1]))
