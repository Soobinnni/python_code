# https://school.programmers.co.kr/learn/courses/30/lessons/120880

# n으로부터의 거리가 같다면 더 큰 수를 앞에 오도록 배치
def solution(numlist, n):
    return [num for _, num in sorted([(abs(num - n), num) for num in numlist], key = lambda x: (x[0], -x[1]))]

def solution_2(numlist, n):
    return sorted(numlist, key = lambda x: (abs(n-x), -x))

print(solution([1, 2, 3, 4, 5, 6], 4)) # [4, 5, 3, 6, 2, 1]
print(solution([10000,20,36,47,40,6,10,7000], 30)) # [36, 40, 20, 47, 10, 6, 7000, 10000]