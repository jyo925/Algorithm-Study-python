# 1249. Minimum Remove to Make Valid Parentheses


class Solution:
    def minRemoveToMakeValid1(self, s: str) -> str:
        s = list(s)
        stack = []
        cur = 0

        for _ in range(len(s)):
            if not s[cur].isalpha():

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
    # 문자를 cur에 쌓아간다.
    # 열린괄호를 만나면 그동안 쌓은 문자를 stack에 저장한다. -> 닫힌 괄호를 하나 만날 때 마다 한개씩 꺼냄
    # 괄호 다음부터 다시 문자를 쌓아간다.
    # 닫힌 괄호를 만나면 stack에서 하나 꺼내서 + (cur)
    def minRemoveToMakeValid2(self, s: str) -> str:

        stack, cur = [], ''
        for c in s:
            if c == '(':
                stack += [cur]
                cur = ''
            elif c == ')':
                if stack:
                    cur = stack.pop() + '(' + cur + ')'
            else:
                cur += c
        # lee((s(t) 처럼 열린 괄호가 많은 경우
        while stack:
            cur = stack.pop() + cur

        return cur


print(Solution.minRemoveToMakeValid2('', "lee(t(c)o)de)"))
print(Solution.minRemoveToMakeValid1('', "))(("))
