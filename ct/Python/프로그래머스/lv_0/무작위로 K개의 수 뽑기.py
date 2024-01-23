# https://school.programmers.co.kr/learn/courses/30/lessons/181858

def solution(arr, k):
    ans = []
    for a in arr:
        if a not in ans:
            ans.append(a)
        if len(ans) == k:
            break
    if len(ans) < k:
        ans += [-1] * (k - len(ans))

    return ans


def solution_2(arr, k):
    ans = []
    for a in arr:
        if a not in ans:
            ans.append(a)
        if len(ans) == k:
            break

    return ans + [-1] * (k - len(ans))

print(solution([0, 1, 1, 2, 2, 3], 3)) # result = [0, 1, 2]
print(solution([0, 1, 1, 1, 1], 4)) # result = [0, 1, -1, -1]