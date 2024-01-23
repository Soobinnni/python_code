# https://school.programmers.co.kr/learn/courses/30/lessons/181890

def solution(str_list):
    for i, st in enumerate(str_list):
        if st == 'l':
            return str_list[:i]
        if st == 'r':
            return str_list[i+1:]
    return []

print(solution(["u", "u", "l", "r"])) # result = ["u", "u"]
print(solution(["l"])) # result = []