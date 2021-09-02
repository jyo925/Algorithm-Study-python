# 394. Decode String
# 닫힌 괄호를 만나면 pop(다음 바깥 문자열) + (현재문자 * pop 숫자(현재문자의 반복횟수))
# 그리고 이 결과를 다음 바깥 괄호의 현재 문자로 업데이트

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num_stack = []

        cur_num = 0
        cur_str = '' # 괄호 안에서 cur문자를 나타낼거임
        for c in s:
            if c == '[':
                stack.append(cur_str)
                num_stack.append(cur_num)
                cur_str = ''
                cur_num = 0
                continue

            elif c == ']':
                prev_str = stack.pop()
                num = num_stack.pop()
                cur_str = prev_str + num * cur_str
                continue

            if c.isdigit():
                cur_num = cur_num * 10 + int(c)
            else:
                cur_str += c

        return cur_str


print(Solution.decodeString('', "3[a2[c]]"))
