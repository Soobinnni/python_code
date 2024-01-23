# https://school.programmers.co.kr/learn/courses/30/lessons/181902

def solution(my_string):
    alphabet = [0] * (26 * 2)
    for st in my_string:
        if st.isupper():
            alphabet[ord(st)-65] += 1
        else:
            alphabet[ord(st)-71] += 1
    return alphabet

print(solution("Programmers"))
# result = 	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0]