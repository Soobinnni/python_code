# https://school.programmers.co.kr/learn/courses/30/lessons/120885

def solution(q, r, code):
    return ''.join(code[i] for i in range(r, len(code), q))

def solution_2(q, r, code):
    return code[r::q]

print(solution(3, 1, "qjnwezgrpirldywt")) # result = "jerry"
print(solution(1, 0, "programmers")) # result = "programmers"