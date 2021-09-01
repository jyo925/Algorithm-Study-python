# 20. Valid Parentheses
# { [ ( 이면 stack에 삽입한다.
# ) ] } 이면 stack에서 pop()하여 비교
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in ('(', '{', '['):
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                tmp = stack.pop()
                if tmp == '(' and i != ')':
                    return False
                if tmp == '[' and i != ']':
                    return False
                if tmp == '{' and i != '}':
                    return False

        if len(stack) != 0:
            return False

        return True


print(Solution.isValid('', "(((())"))
