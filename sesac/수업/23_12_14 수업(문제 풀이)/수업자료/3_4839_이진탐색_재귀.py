def binary_search(l, r, target, cnt):
    c = int((l + r) / 2)

    if c == target:
        return cnt

    if c > target:
        return binary_search(l, c, target, cnt+1)

    elif c < target:
        return binary_search(c, r, target, cnt+1)

for tc in range(1, int(input()) + 1):
    p, a, b = map(int, input().split())

    A = binary_search(1, p, a, 1)
    B = binary_search(1, p, b, 1)
    ans = 0 if A == B else 'A' if A < B else 'B'

    print(f'#{tc} {ans}')