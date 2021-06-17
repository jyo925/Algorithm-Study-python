import sys

# 합이 같은 부분집합(DFS)
sys.stdin = open("input.txt", 'r')


# def DFS(x):
#     t0 = 0
#     t1 = 0
#     if x == n:
#         for i in range(n):
#             if ch[i] == 1:
#                 t1 += nums[i]
#             else:
#                 t0 += nums[i]
#         if t0 == t1:
#             return True
#
#     else:
#         ch[x] = 1
#         if DFS(x + 1):
#             return True
#         ch[x] = 0
#         if DFS(x + 1):
#             return True
#
#
# if __name__ == "__main__":
#     n = int(input())
#     nums = list(map(int, input().split()))
#     # 원소에 포함되는 경우 1 아닌경우 0
#     ch = [0] * n
#
#     if DFS(0):
#         print("YES")
#     else:
#         print("NO")


# 코드 개선
# 서로소 집합 2개의 합계를 게산할 필요 X -> total - sum(집합) 값으로 비교
# sys.exit(0)을 사용하면 시스템 종료로 재귀 탈출 가능


def DFS(L, s):  # L은 인덱스, s는 sum
    if s > total // 2:
        return
    if L == n:
        if s == (total - s):
            print("YES")
            sys.exit(0)
    else:
        DFS(L + 1, s + a[L])
        DFS(L + 1, s)


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0, 0)
    print("NO")
