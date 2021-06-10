from collections import deque


def solution(priorities, location):
    alpha = list(map(chr, range(97, 97 + len(priorities))))
    answer_alpha = alpha[location]
    result = []
    q = deque((alpha[i], priorities[i]) for i in range(len(priorities)))

    # 큐가 빌때까지 계속 확인
    # 큐에서 꺼낸 값과
    # 남은 큐의 중요도 값 중에 더 큰게 있으면 꺼낸 값을 맨뒤에 다시 삽입
    # 없으면 result에 추가
    while q:
        tmp = q.popleft()
        if not q:
            result.append(tmp[0])
            break
        max_priorities = max(q, key=lambda x: x[1])
        if tmp[1] < max_priorities[1]:
            q.append(tmp)
        else:
            result.append(tmp[0])

    return result.index(answer_alpha) + 1


# ABCD 알파벳으로 변환할 필요 없었음
# any를 사용하면 더 깔끔함
# any란? 인자로 받은 반복가능한 자료형(iterable)중 단 하나라도 참이 있으면 Ture 반환
def solution2(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
