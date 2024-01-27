# https://school.programmers.co.kr/learn/courses/30/lessons/181904

def solution(my_string, m, c):
    return ''.join(my_string[i + (c-1)] for i in range(0, len(my_string), m))

def solution_2(my_string, m, c):
    return my_string[c-1::m]


print(solution("ihrhbakrfpndopljhygc", 4, 2)) # result = "happy"
print(solution("programmers", 1, 1)) # result = "programmers"