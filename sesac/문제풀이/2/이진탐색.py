def binary_search(num, target):
    cnt, low, high = 0, 1, num
    mid = int((low+high) / 2)

    while mid != target:
        if mid > target:
            high = mid
            mid = int((low+high) / 2)
        elif mid < target:
            low = mid
            mid = int((low+high) / 2)
        cnt += 1

    return cnt

for test_case in range(1, int(input())+1):
    p, a, b = map(int, input().split())
    a_result = binary_search(p,a)
    b_result = binary_search(p,b)

    ans = 0 if a_result == b_result else 'A' if a_result < b_result else 'B'

    print(f"#{test_case} {ans}")

