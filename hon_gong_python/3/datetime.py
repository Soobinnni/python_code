import datetime
import pytz

#pytz : 파이썬에서 타임존을 구할 때 쓰는 모듈
seoul = pytz.timezone("Asia/Seoul")
#datetime : 파이썬에서 날짜와 시간을 구할 때 쓰는 모듈
now = datetime.datetime.now(seoul)

print(now)

year = now.year
month = now.month
day = now.day

print(f"{year}년 {month}월 {day}일")
print("{0}년 {2}일 {1}월".format(year, month, day))