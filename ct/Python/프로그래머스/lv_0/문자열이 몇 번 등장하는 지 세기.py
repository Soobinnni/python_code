# https://school.programmers.co.kr/learn/courses/30/lessons/181871

def solution(myString, pat):
    if pat not in myString:
        return 0
    len_pat = len(pat)
    return sum(1 for i in range(len(myString) - len_pat + 1) if myString[i : i + len_pat] == pat)

print(solution("banana", "ana")) # result = 2
print(solution("aaaa", "aa")) # result = 3