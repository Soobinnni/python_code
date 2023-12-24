# https://www.acmicpc.net/problem/10872

def factorial(N):
    if N == 0:
        return 1

    return N * factorial(N-1)

def factorial2(N):
    if N <= 1:
        return 1

    return N * factorial(N-1)

N = int(input())
print(factorial2(N))