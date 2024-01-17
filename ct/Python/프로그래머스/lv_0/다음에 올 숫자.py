# https://school.programmers.co.kr/learn/courses/30/lessons/120924

def solution(common):
    a, b, c = common[0], common[1], common[2]
    if (b - a) == (c - b):
        return common[-1] + (b - a)
    else:
        return common[-1] * int(b/a)


test_case1 = [1,2,3,4]
test_case2 = [2,4,8]
test_case3 = [2,2,2]
test_case4 = [2,-4,8]

print(solution(test_case1)) # result = 5
print(solution(test_case2)) # result = 16
print(solution(test_case3)) # result = 2
print(solution(test_case4)) # result = -2