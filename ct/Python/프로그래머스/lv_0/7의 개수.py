# https://school.programmers.co.kr/learn/courses/30/lessons/120912

def solution(array):
    return sum(str(a).count('7') for a in array)

def solution_2(array):
    return str(array).count('7')

print(solution([7, 77, 17])) # result = 4
print(solution([10, 29])) # result = 0