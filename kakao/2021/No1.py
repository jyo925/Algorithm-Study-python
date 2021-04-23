# 2021 카카오 신입공채 1차 온라인 코딩 테스트 
# 1번 문제
import re


def solution(new_id):
    answer = ''
    if not new_id.islower() and new_id != "":
        answer = new_id.lower()
    else:
        answer = new_id

    if any(i in answer for i in "~!@#$%^&*()=+[{]}:?,<>/"):
        old = answer
        answer = re.sub('[~=+,#/\?:^$@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>\{\}:`\'…》]', '', answer)

    p = re.compile('[.]{2}')
    m = p.search(answer)
    if m is not None:
        old = answer
        s = answer
        while m is not None:
            i, j = m.span()
            tmp = answer[i: j]
            answer = answer.replace(tmp, ".")
            m = p.search(answer)

    if answer[0] == ".":
        answer = answer[1:]

    if len(answer) > 1 and answer[-1] == ".":
        answer = answer[:-1]

    if answer == "":
        answer = 'a'

    old = answer
    if len(answer) >= 16:
        answer = answer[:15]

        if answer[0] == ".":
            answer = answer[1:]
        elif answer[-1] == ".":
            answer = answer[:-1]

    if 3 > len(answer) > 0:
        while len(answer) < 3:
            answer = answer + answer[-1]

    return answer


print(solution("=.="))
