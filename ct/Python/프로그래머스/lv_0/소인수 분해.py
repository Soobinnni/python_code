# https://school.programmers.co.kr/learn/courses/30/lessons/120852

# 틀린 답
def solution(n):
    factors = set()
    i = 2
    while i <= n:
        if n % i == 0:
            factors.add(i)
            n = n / i
        else:
            i = i + 1
    return list(factors)

def solution_2(n):
    answer = []
    d = 2
    while d <= n:
        if n % d == 0:
            n /= d
            if d not in answer:
                answer.append(d)
        else:
            d += 1
    return answer

def solution_3(n):
    answer = []

    x = 2
    while x <= n:
        if n % x == 0:
            if x not in answer:
                answer.append(x)
            n //= x
        else:
            x += 1
    return answer


print(solution(12)) # result = [2, 3]
print(solution(17)) # result = [17]
print(solution(420)) # result = [2, 3, 5, 7]