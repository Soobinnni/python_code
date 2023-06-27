# 오전 오후 구분하는 프로그램
from pytz import timezone
from datetime import datetime

today = datetime.now(timezone('Asia/Seoul'))

print(f"현재 시각은 {today.hour}시입니다!")
if today.hour < 12 :
    print('오전입니다!')
else :
    print('오후입니다!')
