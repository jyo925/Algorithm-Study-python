import sys

# 휴가(삼성 SW역량평가 기출문제 : DFS활용)
# t 소요 일자 p 페이
# 인덱스 번호를 날짜로 사용
# n번째날 상담을 하느냐 하지 않느냐로 구분 상태트리 그리기

sys.stdin = open("input.txt", 'r')


# 최대 O(2^n)
def DFS(day, pay):
    global res

    if day == n + 1:
        if pay > res:
            res = pay
    else:
        # day번째 상담을 한다고 했을 때 day번째 상담일수를 더한 값이 n+1보다 작거나 같아야 함
        # 이때만 가지가 뻗어 나가도록
        if day + g[day][0] <= n + 1:
            DFS(day + g[day][0], pay + g[day][1])
        # 상담을 할 수 없으면 날짜만 하루 지나도록, 페이는 그대로 유지
        DFS(day + 1, pay)


if __name__ == "__main__":
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]
    g.insert(0, [0, 0])
    res = -2147000000
    DFS(1, 0)
    print(res)
