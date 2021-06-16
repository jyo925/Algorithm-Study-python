import sys

# 아나그램
# 리스트 해쉬(C++처럼 구현)
sys.stdin = open("input.txt", 'r')

w1 = input()
w2 = input()
str1 = [0] * 52 #대문자 소문자 총 52개
str2 = [0] * 52

for x in w1:
    if x.isupper():
        # ord는 문자를 아스키 코드로 변환
        # 대문자 A 기준 65 ~ 90
        # 소문자 A 기준 97 ~ 122
        str1[ord(x) - 65] += 1 # 대문자는 인덱스 0 ~ 25, 소문자는 26 ~ 51이 오도록
    else:
        str1[ord(x) - 71] += 1

for x in w2:
    if x.isupper():
        str2[ord(x) - 65] += 1
    else:
        str2[ord(x) - 71] += 1


for i in range(52):
    if str1[i] != str2[i]:
        print("NO")
        break
else:
    print("YES")
