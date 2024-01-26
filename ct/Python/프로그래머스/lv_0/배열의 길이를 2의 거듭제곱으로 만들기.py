# https://school.programmers.co.kr/learn/courses/30/lessons/181857

def solution(arr):
    arr_len = len(arr)
    n = 0
    while arr_len > (1 << n): n += 1

    return arr + [0] * ((1 << n) - arr_len) if arr_len!= 1 else arr

print(solution([1, 2, 3, 4, 5, 6])) # result = [1, 2, 3, 4, 5, 6, 0, 0]
print(solution([58, 172, 746, 89])) # result = [58, 172, 746, 89]