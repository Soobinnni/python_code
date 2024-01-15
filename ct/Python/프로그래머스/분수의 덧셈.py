# https://school.programmers.co.kr/learn/courses/30/lessons/120808
# 최대 공약수 구하기: https://ko.wikipedia.org/wiki/%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C_%ED%98%B8%EC%A0%9C%EB%B2%95

# math 모듈 사용하기
import math
def solution_1(numer1, denom1, numer2, denom2):
    denom = denom1 * denom2
    numer = (numer1 * denom2) + (numer2 * denom1)

    division_num = math.gcd(denom, numer)

    return [int(numer/division_num), int(denom/division_num)]


# 최대공약수 직접 구현
def get_gcd(num1, num2):
    a, b = (num1, num2) if num1 <= num2 else (num2, num1)
    while b > 0:
        a, b = b, a % b
    return a
def solution_2(numer1, denom1, numer2, denom2):
    denom = denom1 * denom2
    numer = (numer1 * denom2) + (numer2 * denom1)
    division_num = get_gcd(denom, numer)

    return [int(numer/division_num), int(denom/division_num)]

test_case1 = solution_2(1, 2, 3, 4)
test_case2 = solution_2(9, 2, 1, 3)

print(test_case1) # result = [5, 4]
print(test_case2) # result = [29, 6]