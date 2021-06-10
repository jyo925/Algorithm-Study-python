import sys

# 스도쿠 검사
# 전략: 그룹별 검사는 4중 for문을 사용하는게 맞았음
sys.stdin = open("input.txt", 'r')


def check(a):
    # 행과 열을 탐색
    for i in range(9):
        ch_row = [0] * 10
        ch_col = [0] * 10
        for j in range(9):
            ch_row[a[i][j]] = 1
            ch_col[a[j][i]] = 1
        if sum(ch_row) != 9 or sum(ch_col) != 9:
            return False
    # 그룹 검사
    for i in range(3): # 0 1 2
        for j in range(3): # 0 1 2
            ch_box = [0] * 10
            for k in range(3): # 0 1 2
                for s in range(3): # 0 1 2
                    # i 와 j에 따라서 9개 그룹 계산
                    # 0행 0열, 0행 3열, 0행 6열
                    # 3행 0열, 3행 3열, 3행 6열
                    # 6행 0열, 6행 3열, 6행 6열
                    ch_box[a[i * 3 + k][j * 3 + s]] = 1
            if sum(ch_box) != 9:
                return False
    return True


puzzle = [list(map(int, input().split())) for _ in range(9)]

if check(puzzle):
    print("YES")
else:
    print("NO")
