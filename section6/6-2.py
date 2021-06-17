import sys

# 이진트리 순회(깊이우선탐색 DFS)
# 전위순회 부 왼 오
# 중위순회 왼 부 오
# 후위순회 왼 오 부
sys.stdin = open("input.txt", 'r')


def DFS(x):
    if x > 7:
        return
    else:
        print(x, end=' ')
        DFS(x * 2)  # 왼쪽 자식 호출
        DFS(x * 2 + 1)  # 오른쪽 자식 호출


if __name__ == "__main__":
    DFS(1)
