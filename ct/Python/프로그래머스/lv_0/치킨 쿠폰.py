# https://school.programmers.co.kr/learn/courses/30/lessons/120884

def solution(chicken):
    ans = 0
    remain_coupon = chicken # 치킨 개수만큼 쿠폰이 생김

    while remain_coupon >= 10:
        coupon_chicken = remain_coupon // 10
        remain_coupon = coupon_chicken + (remain_coupon % 10)

        ans += coupon_chicken

    return ans

print(solution(100)) # result = 11
print(solution(1081)) # result = 120