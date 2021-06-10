import sys

# 격자판 회문수
# 전략:
sys.stdin = open("input.txt", 'r')

board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0

# 회문 체크
def check(a):
    for s in range(len(a) // 2):
        if a.pop() != a.pop(0):
            return False
    return True


for i in range(7):
    for j in range(3):  # 0, 1, 2
        row = [board[i][j + k] for k in range(5)]
        if check(row):
            cnt += 1
        col = [board[j + k][i] for k in range(5)]
        if check(col):
            cnt += 1

print(cnt)

# 다른 풀이(슬라이싱 사용)
count = 0
for i in range(3):
    for j in range(7):
        tmp = board[j][i:i + 5]
        if tmp == tmp[::-1]:
            count += 1
    # col은 슬라이싱 사용 X 양 끝에 있는 수 2개를 각각 비교
        for k in range(2):
            if board[i + k][j] != board[i + 5 - k - 1][j]:
                break
        else:
            count += 1

print(count)
