# https://school.programmers.co.kr/learn/courses/30/lessons/181872

# 5 ≤ myString ≤ 20
# 1 ≤ pat ≤ 5
# pat은 반드시 myString의 부분 문자열로 주어집니다.
# myString과 pat에 등장하는 알파벳은 대문자와 소문자를 구분합니다.

def solution(myString, pat):
    reverse_myString = myString[::-1]
    reverse_pat = pat[::-1]

    for i in range(len(myString)):
        if reverse_myString[i:i+len(pat)] == reverse_pat:
            return myString[:len(myString) - i]


def solution_2(myString, pat):
    idx = len(myString) - (myString[::-1].index(pat[::-1]))
    return myString[:idx]

print(solution("AbCdEFG", "dE")) # result = "AbCdE"
print(solution("AAAAaaaa", "a")) # result = "AAAAaaaa"