from collections import deque
import math


def solution(progresses, speeds):
    answer = []
    q = deque((progresses[i], speeds[i]) for i in range(len(progresses)))

    start = q.popleft()
    day = math.ceil(((100 - start[0]) / start[1]))
    cnt = 1

    while q:
        tmp = q.popleft()
        tmp_days = math.ceil(((100 - tmp[0]) / tmp[1]))
        if day >= tmp_days:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            day = tmp_days

    answer.append(cnt)
    return answer


# print(solution([93, 30, 55], [21, 25, 20]))
print(solution([5, 5, 5], [1, 30, 5]))
# print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
# print(solution([40, 93, 30, 55, 60, 65], [60, 1, 30, 5 , 10, 7]))
# print(solution([93, 30, 55, 60, 40, 65], [1, 30, 5 , 10, 60, 7]))
