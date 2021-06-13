import sys
# 쇠막대기
sys.stdin = open("input.txt", 'r')

# ( 이면 스택에 넣는다.
#  ) 이면 막대 정보에서 바로 앞 막대가 무엇인지 학인
#  1. ( 이 나오면 레이저 -> pop 후 sum += len(스택) 스택에 남아있는 개수가 막대이므로 남아있는 막대 개수만큼 조각이 생성
#  2. ) 나오면 막대기 끝 지점 -> pop 후 sum += 1(막대 마지막 조각)
bars = input()
stack = []
cnt = 0

for i in range(len(bars)):
    if bars[i] == '(':
        stack.append(bars[i])
    else:
        tmp = bars[i-1]
        stack.pop()
        if tmp == '(':
            cnt += len(stack)
        else:
            cnt += 1

print(cnt)





