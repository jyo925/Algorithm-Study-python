# 통과했지만 테스트 케이스 하나가 9초가 걸림
# sum() -> o(n) 이므로 이부분을 개선


def solution(bridge_length, weight, truck_weights):
    queue = [0] * bridge_length
    count = 0
    cur_weight = 0

    while truck_weights:
        tmp1 = queue.pop(0)
        if tmp1 != 0:
            cur_weight -= tmp1
        if truck_weights[0] <= weight - cur_weight:
            tmp2 = truck_weights.pop(0)
            queue.append(tmp2)
            cur_weight += tmp2
        else:
            queue.append(0)
        count += 1

    while queue:
        queue.pop()
        count += 1

    return count


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
