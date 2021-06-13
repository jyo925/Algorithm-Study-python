# 다시 생각하기 시간초과 대박

def solution(prices):
    answer = []

    p = 1
    while prices:
        if len(prices) == 1:
            answer.append(0)
            break

        if p == len(prices) - 1:
            answer.append(p)
            prices.pop(0)
            p = 1
            continue

        if prices[0] <= prices[p]:
            p += 1
        else:
            answer.append(p)
            prices.pop(0)
            p = 1
    return answer


print(solution([1, 2, 3, 2, 3]))
