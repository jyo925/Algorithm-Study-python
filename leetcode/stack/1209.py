# 1209. Remove All Adjacent Duplicates in String II
# 두 개의 스택 사용

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack, count = [], []

        for i in s:
            if not stack:
                stack.append(i)
                count.append(1)
                continue

            if i == stack[-1]:
                tmp = count[-1]
                if tmp == k - 1:
                    for _ in range(tmp):
                        stack.pop()
                    count.pop()
                else:
                    stack.append(i)
                    count[-1] = tmp + 1
            else:
                stack.append(i)
                count.append(1)

        return ''.join(stack)


print(Solution.removeDuplicates('', "deeedbbcccbdaa", 3))
