# https://school.programmers.co.kr/learn/courses/30/lessons/181830

def solution(arr):
    x_len = len(arr[0])
    y_len = len(arr)

    if x_len < y_len:
        for a in arr:
            a += [0] * (y_len - x_len)
    else:
        for _ in range(x_len - y_len):
            arr.append([0] * x_len)

    return arr

print(solution([[572, 22, 37], [287, 726, 384], [85, 137, 292], [487, 13, 876]]))
# result = [[572, 22, 37, 0], [287, 726, 384, 0], [85, 137, 292, 0], [487, 13, 876, 0]]

print(solution([[57, 192, 534, 2], [9, 345, 192, 999]]))
# result = [[57, 192, 534, 2], [9, 345, 192, 999], [0, 0, 0, 0], [0, 0, 0, 0]]

print(solution([[1, 2], [3, 4]]))
# result = [[1, 2], [3, 4]]