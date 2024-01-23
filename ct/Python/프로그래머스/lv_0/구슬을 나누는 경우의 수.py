# https://school.programmers.co.kr/learn/courses/30/lessons/120840

def fac(n, ret = 1):
    for i in range(2, n + 1): ret *= i
    return ret

def solution(balls, share):
    return int((fac(balls)) / (fac(balls - share)*fac(share)))

print(solution(3, 2)) # result = 3
print(solution(5, 3)) # result = 10