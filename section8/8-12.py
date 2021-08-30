import sys

# 플로이드 워셜 알고리즘
# 모든 정점에서 모든 정점으로 가는 최단거리
# 2차원 배열 이용, 점화식
# 중간 경유지는 순열로 존재
# dis[i][j] 와 dis[i][k] + dis[k][j] 중에서 min값을 선택
# k=1,2,3,,일 때, i, j 이중 for문 수행 ===> 즉 i에서 j까지 갈 때 중간정점 k를 거쳐가는 경우 거리를 모두 확인하여 최소값으로 업데이트

sys.stdin = open("input.txt", 'r')

if __name__ == "__main__":
    n, m = map(int, input().split())

    # 배열 초기화 작업
    dis = [[5000] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dis[i][i] = 0
    # 직행했을 경우
    for i in range(m):
        a, b, c = map(int, input().split())
        dis[a][b] = c

    #플로이드 워셜 적용
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

    #출력
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dis[i][j] == 5000:
                print("M", end=' ')
            else:
                print(dis[i][j], end=' ')
        print()
