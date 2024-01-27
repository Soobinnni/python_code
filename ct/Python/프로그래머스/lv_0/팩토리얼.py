# https://school.programmers.co.kr/learn/courses/30/lessons/120848

# i! ≤ n

def solution(n):
    multiple_num = 0
    result = 1
    while result <= n:
        multiple_num += 1
        result *= multiple_num

    return multiple_num - 1

print(solution(3628800)) # result = 10
print(solution(7)) # result = 3