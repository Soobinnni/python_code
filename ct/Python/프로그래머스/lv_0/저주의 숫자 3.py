# https://school.programmers.co.kr/learn/courses/30/lessons/120871
def get_next_num(num):
    if ('3' not in str(num)) and (num % 3 != 0):
        return num

    while '3' in str(num):
        return get_next_num(num+1)

    while num % 3 == 0:
        return get_next_num(num+1)

def solution(n):
    ans = 0
    for i in range(n):
        ans += 1
        ans = get_next_num(ans)

    return ans


# 다른 사람 풀이
def solution_2(n):
    answer = 0
    for _ in range(n):
        answer += 1
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1

    return answer

print(solution(15)) # result = 25
print(solution(40)) # result = 76