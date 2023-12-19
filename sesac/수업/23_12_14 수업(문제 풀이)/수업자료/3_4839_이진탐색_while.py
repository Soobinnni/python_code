def binary_search(P, target):
    l, r = 1, P
    cnt = 0

    while c != target:
        c = int((l + r) / 2)
        if c > target:
            r = c

        elif c < target:
            l = c

        cnt += 1

    return cnt

for tc in range(1, int(input()) + 1):
    p, a, b = map(int, input().split())

    A = binary_search(p, a)
    B = binary_search(p, b)
    ans = 0 if A == B else 'A' if A < B else 'B'

    print(f'#{tc} {ans}')