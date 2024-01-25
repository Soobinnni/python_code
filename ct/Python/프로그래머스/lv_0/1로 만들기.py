# https://school.programmers.co.kr/learn/courses/30/lessons/181880

def solution(num_list):
    cnt = 0
    for n in num_list:
        num = n
        while num != 1:
            num = int(num / 2)
            cnt += 1
    return cnt

def solution_2(num_list):
    return sum(len(bin(i)) - 3 for i in num_list)

print(solution_2([12, 4, 15, 1, 14])) # result = 11