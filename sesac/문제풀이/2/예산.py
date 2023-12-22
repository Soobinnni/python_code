n = int(input())
reqs = list(map(int, input().split()))
M = int(input())

def recursive_func(l, r):
    if l > r:
        return r

    c = (l+r)//2

    budget = 0
    for re in reqs:
        if c >= re:
            budget += re
        else:
            budget += c

    if budget < M:
        return recursive_func(c+1, r)
    else:
        return recursive_func(l, c-1)

print(recursive_func(0, max(reqs)))