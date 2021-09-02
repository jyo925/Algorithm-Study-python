# 227. Basic Calculator II
# 풀이틀림
# 문제점: -를 숫자 스택에 반영하여 넣고 마지막에 스택에 있는 모든 숫자를 합하면 됨

from math import floor


class Solution:
    # def calculate(self, s: str) -> int:
    #
    #     num = []
    #     operator = []
    #
    #     for i in s:
    #         # print(num)
    #         if i == ' ':
    #             continue
    #
    #         if i.isdigit():
    #             i = int(i)
    #             if len(num) > len(operator):
    #                 num[-1] = num[-1] * (10 * (len(num) - len(operator))) + i
    #
    #                 continue
    #             # 숫자인 경우 스택에 삽입
    #             if operator and operator[-1] in ('/', '*'):
    #                 o = operator.pop()
    #                 prev_num = num.pop()
    #                 if o == '/':
    #                     num.append(prev_num // i)
    #                 elif o == '*':
    #                     num.append(prev_num * i)
    #             else:
    #                 num.append(i)
    #         else:
    #             operator.append(i)
    #
    #     while operator:
    #         num2 = num.pop()
    #         num1 = num.pop()
    #         o = operator.pop()
    #         if o == '+':
    #             num.append(num1 + num2)
    #         else:
    #             print(num2, num1)
    #
    #             num.append(num2 - num1)
    #
    #     return num[-1]

    # print(Solution.calculate('', " 3/2 "))
    # print(Solution.calculate('', "42"))

    # 잘못품 -> 마지막이 9/10인경우 9/1을 먼저 계산하도록 코드를 짰음
    # def calculate(self, s: str) -> int:
    #
    #     stack = []
    #     operator = ''
    #     isNum = False
    #
    #     for i in s:
    #         print(stack)
    #         if i == ' ':
    #             continue
    #
    #         if i.isdigit():
    #             i = int(i)
    #             if isNum:
    #                 if stack[-1] > 0:
    #                     stack[-1] = stack[-1] * 10 + i
    #                 else:
    #                     stack[-1] = stack[-1] * 10 - i
    #                 continue
    #
    #             if operator == '':
    #                 stack.append(i)
    #             elif operator == '-':
    #                 stack.append(-i)
    #             elif operator == '*':
    #                 stack[-1] = stack[-1] * i
    #             elif operator == '/':
    #                 stack[-1] = stack[-1] // i
    #                 print(stack[-1])
    #                 if stack[-1] < 0:
    #                     stack[-1] += 1
    #
    #             else:
    #                 stack.append(i)
    #             operator = ''
    #             isNum = True
    #
    #         else:  # 연산자 들어오는경우
    #             operator = i
    #             isNum = False
    #
    #     print(stack)
    #     return sum(stack)

    def calculate(self, s: str) -> int:
        s += '+'  # additional last op
        stack = []

        cur_num = 0
        prev_op = '+'
        for c in s:
            if c.isdigit():
                cur_num = cur_num * 10 + int(c)

            elif c == ' ':
                continue

            else:  # ops
                if prev_op == '+':
                    stack.append(cur_num)

                elif prev_op == '-':
                    stack.append(-cur_num)

                elif prev_op == '*':
                    stack[-1] = stack[-1] * cur_num

                elif prev_op == '/':
                    stack[-1] = int(stack[-1] / cur_num)

                cur_num = 0
                prev_op = c

        return sum(stack)


# print(Solution.calculate('', "0-2147483647"))
# print(Solution.calculate('', " 3+5 / 2 "))
# print(Solution.calculate('', " 3/2 "))
# print(Solution.calculate('', "14-3/2"))
print(Solution.calculate('', "1*2-3/4+5*6-7*8+9/10"))

