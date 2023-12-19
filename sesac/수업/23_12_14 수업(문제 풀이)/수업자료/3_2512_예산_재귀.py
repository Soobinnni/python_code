import sys
input = sys.stdin.readline

N = int(input())
reqs = list(map(int, input().split()))
M = int(input())

l, r = 0, max(reqs)

def binary_search(l, r):
    if l > r:
        return r
    
    c = (l + r) // 2

    budget = 0
    for req in reqs:
        if req <= c:
            budget += req

        else:
            budget += c

    if budget > M:
        return binary_search(l, c - 1)

    else:
        return binary_search(c + 1, r)

print(binary_search(0, max(reqs)))