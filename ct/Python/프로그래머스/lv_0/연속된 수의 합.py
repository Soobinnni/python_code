# https://school.programmers.co.kr/learn/courses/30/lessons/120923
def solution(num, total):
    if num == 1:
        return [total]

    for i in range(abs(total - num + 1)):
        num_arr = [i + j for j in range(num)]
        if total < sum(num_arr):
            for j in range(1, num):
                num_arr.pop(-1)
                num_arr.append(-j)
                num_arr.sort()
                if total == sum(num_arr):
                    return num_arr

        if total == sum(num_arr):
            return num_arr

print('#1', solution(3, 12)) # result = [3, 4, 5]
print('#2', solution(5, 15)) # result = [1, 2, 3, 4, 5]
print('#3', solution(4, 14)) # result = [2, 3, 4, 5]
print('#4', solution(5, 5)) # result = [-1, 0, 1, 2, 3]
print('#5', solution(3, 3)) # result = [0, 1, 2]
print('#5', solution(5, 0)) # result = [-2, -1, 0, 1, 2]