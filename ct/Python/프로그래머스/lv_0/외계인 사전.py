# https://school.programmers.co.kr/learn/courses/30/lessons/120869

def solution(spell, dic):
    for d in dic:
        bool_arr = [False] * len(spell)
        for i, s in enumerate(spell):
            if d.count(s) == 1: bool_arr[i] = True
        if not(False in bool_arr):
            return 1
    return 2

print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"])) # result = 2
print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"])) # result = 1
print(solution(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"])) # result = 2