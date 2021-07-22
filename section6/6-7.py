import sys

# 동전교환
# L을 동전의 개수로
sys.stdin = open("input.txt", 'r')


def DFS(L, s):
    global min_cnt
    if s > m or L > min_cnt:
        return
    elif m == s:
        min_cnt = L
        return True
    else:
        # 동전의 종류 개수(n)만큼
        for i in range(n):
            # 핵심 시간 단축
            # 5원 3개면 D(3, 15)으로 그 다음 순서들은 D(3, 13) 5원 2개 + 3원 등등 볼 필요가 없음
            if DFS(L + 1, s + coin[i]): 
                break


if __name__ == "__main__":
    min_cnt = 2147000000
    n = int(input())
    coin = list(map(int, input().split()))
    coin.reverse() #동전의 개수가 가장 적어야 하므로 가장 큰 단위부터 확인
    m = int(input())
    DFS(0, 0)
    print(min_cnt)
