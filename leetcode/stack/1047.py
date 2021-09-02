# 1047. Remove All Adjacent Duplicates In String


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = [] # o(n)

        for i in s: # o(n)

            if not stack:
                stack.append(i)
            else:
                if stack[-1] == i :
                    stack.pop()
                else:
                    stack.append(i)

        return ''.join(stack)





print(Solution.removeDuplicates('', "abbaca"))
