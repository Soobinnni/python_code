# https://school.programmers.co.kr/learn/courses/30/lessons/181851

def solution(rank, attendance):
    arr = [rank.index(r) for r in sorted([rank[i] for i, a in enumerate(attendance) if a])]
    return 10000 * arr[0] + 100 * arr[1] + arr[2]

# 10000 × a + 100 × b + c

print(solution([3, 7, 2, 5, 4, 6, 1], [False, True, True, True, True, False, False])) # result = 20403
print(solution([1, 2, 3], [True, True, True])) # result = 102
print(solution([6, 1, 5, 2, 3, 4], [True, False, True, False, False, True])) # result = 50200