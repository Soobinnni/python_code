from pytz import timezone
from datetime import datetime

month = datetime.now(timezone('Asia/Seoul')).month

print(f"현재 {month}월")

if 3 <= month <6 :
    print("봄입니다!")
elif 6 <= month <9 :
    print("여름입니다!")
elif 9<= month < 12 :
    print("가을입니다!")
else :
    print("겨울입니다!")