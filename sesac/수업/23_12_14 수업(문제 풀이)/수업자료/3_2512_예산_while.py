import sys
input = sys.stdin.readline

N = int(input())
reqs = list(map(int, input().split()))
M = int(input())

l, r = 0, max(reqs)

while l <= r:
    c = (l + r) // 2

    budget = 0
    for req in reqs:
        if req <= c:
            budget += req

        else:
            budget += c

    if budget > M:
        r = c - 1

    else:
        l = c + 1

print(r)