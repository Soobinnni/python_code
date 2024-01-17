# https://school.programmers.co.kr/learn/courses/30/lessons/120863

def solution(polynomial):
    polynomial_list = polynomial.split()
    x = 0
    c = 0
    for po in polynomial_list:
        if po == '+': continue
        if 'x' in po:
            x += int(po[:-1]) if len(po) != 1 else 1
        else:
            c += int(po)
    if not c:
        return f"{x if x!= 1 else ''}x"
    if not x:
        return f"{c}"
    return f"{x if x!= 1 else ''}x + {c}"

test_case1 = "3x + 7 + x"
test_case2 = "x + x + x"
test_case3 = "x + 2"

print(solution(test_case1)) # result = "4x + 7"
print(solution(test_case2)) # result = "3x"
print(solution(test_case3)) # result = "x + 2"