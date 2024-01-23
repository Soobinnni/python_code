# https://school.programmers.co.kr/learn/courses/30/lessons/120913

def solution(my_str, n):
    answer = ''
    for i in range(int(len(my_str) / n) + 1):
        answer += my_str[(i * n) : ((i+1)*n)] + ' '
    return answer.strip().split()

def solution_2(my_str, n):
    return ''.join([my_str[(i * n) : ((i+1)*n)] + ' ' for i in range(int(len(my_str) / n) + 1)]).strip().split()

def solution_3(my_str, n):
    return [my_str[i : (i + n)] for i in range(0, len(my_str), n)]

print(solution("abc1Addfggg4556b", 6)) # result = ["abc1Ad", "dfggg4", "556b"]
print(solution("abcdef123", 3)) # result = ["abc", "def", "123"]