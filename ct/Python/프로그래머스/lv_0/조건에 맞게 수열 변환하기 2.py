# https://school.programmers.co.kr/learn/courses/30/lessons/181881

def solution(arr):
    cnt = -1
    change = True

    while change:
        cnt += 1
        change = False
        for i in range(len(arr)):
            if (50 <= arr[i]) and (arr[i] % 2 == 0):
                arr[i] = int(arr[i] / 2)
                change = True
            if (50 > arr[i]) and (arr[i] % 2):
                arr[i] = arr[i] * 2 + 1
                change = True
    return cnt

print(solution([1, 2, 3, 100, 99, 98])) # result = 5