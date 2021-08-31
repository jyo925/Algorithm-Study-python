# 시간 측정
import datetime
import functools

start_time = datetime.datetime.now()
# 블라블라 코드 작성
print(datetime.datetime.now() - start_time)

# 숫자 리스트를 문자열로 합치기
numbers = [3, 30, 34, 5, 9]
print(str(int(''.join(str(e) for e in numbers))))
print(str(int(''.join(map(str, numbers)))))

