# https://school.programmers.co.kr/learn/courses/30/lessons/120853

def solution(s):
    answer = 0
    s = s.split()
    for i, st in enumerate(s):
        if st != 'Z':
            answer += int(st)
        else:
            answer -= int(s[i-1])
    return answer

print(solution("1 2 Z 3")) # result = 4
print(solution("10 20 30 40")) # result = 100
print(solution("10 Z 20 Z 1")) # result = 1
print(solution("10 Z 20 Z")) # result = 0
print(solution("-1 -2 -3 Z")) # result = -3