from datetime import datetime


#년 월 일 시 분 초
now = datetime.now()

y = now.year
m = now.month
d = now.day
h = now.hour
mm = now.minute
ss = now.second

print("현재, {0}년 {1}월 {2}일 {3}시 {4}분 {5}초".format(y, m, d, h, mm, ss))