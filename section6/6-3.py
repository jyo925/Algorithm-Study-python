import sys


# 부분집합 구하기(DFS)
# 상태트리 그리기
# 1일 때 o,x 1이 o일 때 2 o,x 식으로 뻗어나가기
# sys.stdin = open("input.txt", 'r')


def DFS(x):
    if x == n + 1:
        # 부분집합출력
        for i in range(1, n + 1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
    else:
        ch[x] = 1
        DFS(x + 1)
        ch[x] = 0
        DFS(x + 1)


if __name__ == "__main__":
    n = int(input())
    # ch변수를 사용해서 값을 사용할 때는 1,안 할때는 0
    ch = [0] * (n + 1)
    DFS(1)
