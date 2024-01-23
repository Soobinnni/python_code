# https://school.programmers.co.kr/learn/courses/30/lessons/120843

def solution(numbers, k):
    throw = 0
    for _ in range(1, k): throw += 2
    return numbers[throw % len(numbers)]

def solution_2(numbers, k):
    return numbers[2 * (k-1) % len(numbers)]

print(solution([1, 2, 3, 4], 2)) # result = 3
print(solution([1, 2, 3, 4, 5, 6], 5)) # result = 3
print(solution([1, 2, 3], 3)) # result = 2