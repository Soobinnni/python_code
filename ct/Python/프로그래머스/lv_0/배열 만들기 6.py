# https://school.programmers.co.kr/learn/courses/30/lessons/181859

def solution(arr):
    answer = []
    for i in range(len(arr)):
        answer.append(arr[i]) if (not answer) or (answer[-1] != arr[i]) else answer.pop(-1)

    return answer if answer else [-1]

def solution_2(arr):
    answer = []
    for i in range(len(arr)):
        answer.append(arr[i]) if (not answer) or (answer[-1] != arr[i]) else answer.pop(-1)

    return answer or [-1]

print(solution([0, 1, 1, 1, 0])) # result = [0, 1, 0]
print(solution([0, 1, 0, 1, 0])) # result = [0, 1, 0, 1, 0]
print(solution([0, 1, 1, 0])) # result = [-1]