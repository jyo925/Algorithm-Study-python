# 1249. Minimum Remove to Make Valid Parentheses


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        cur = 0

        for _ in range(len(s)):
            if not s[cur].isalpha():
                # print(s, cur, s[cur], stack)
                if s[cur] == '(':
                    stack.append([cur, s[cur]])
                    cur += 1
                elif s[cur] == ')':
                    if len(stack) == 0:
                        s.pop(cur)
                        continue
                    else:
                        stack.pop()
                        cur += 1
            else:
                cur += 1
        while len(stack) != 0:
            c, v = stack.pop()
            s.pop(c)

        return ''.join(s)


# 다른 풀이
# class Solution:
#     def minRemoveToMakeValid(self, s: str) -> str:
#
#         stack, cur = [], ''
#         for c in s:
#             if c == '(':
#                 stack += [cur]
#                 cur = ''
#             elif c == ')':
#                 if stack:
#                     cur = stack.pop() + '(' + cur + ')'
#             else:
#                 cur += c
#
#         while stack:
#             cur = stack.pop() + cur
#
#         return cur


print(Solution.minRemoveToMakeValid('', "lee(t(c)o)de)"))
