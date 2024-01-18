# https://school.programmers.co.kr/learn/courses/30/lessons/120921

def solution(A, B):
    ans = 0
    if A == B: return ans

    for _ in range(len(A)-1):
        A = A[-1] + A[:-1]
        ans += 1

        if A == B: return ans
    else:
        return -1

print(solution("hello", "ohell")) # result = 1
print(solution("apple", "elppa")) # result = -1
print(solution("atat", "tata")) # result = 1
print(solution("abc", "abc")) # result = 0
print(solution("abc", "bca")) # result = 2
