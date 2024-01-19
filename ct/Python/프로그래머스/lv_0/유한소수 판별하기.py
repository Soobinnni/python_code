# https://school.programmers.co.kr/learn/courses/30/lessons/120878
from math import gcd

def solution(a, b):
    ans = 1
    if not(a % b) : return ans
    b = int(b / gcd(a, b))
    while b != 1:
        if not(b%2):
            b = b / 2
        elif not(b%5):
            b = b / 5
        elif b == 1:
            break
        else:
            ans = 2
            break
    return ans

# 다른 사람 풀이
def solution_2(a, b):
    b = b / gcd(a, b)

    while b % 2 == 0 : b = b // 2
    while b % 5 == 0 : b = b // 5

    return 1 if b == 1 else 2

print(solution(7, 20)) # result = 1
print(solution(11, 22)) # result = 1
print(solution(12, 21)) # result = 2