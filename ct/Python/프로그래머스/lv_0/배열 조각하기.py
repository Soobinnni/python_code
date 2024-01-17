# https://school.programmers.co.kr/learn/courses/30/lessons/181893

def solution(arr, query):
    for i, q in enumerate(query):
        arr = arr[q:] if i % 2 else arr[:q+1]
    return arr

print(solution([0, 1, 2, 3, 4, 5], [4, 1, 2])) # result = [1,2,3]