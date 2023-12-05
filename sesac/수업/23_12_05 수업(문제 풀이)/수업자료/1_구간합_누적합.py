for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    S = [0]
    s = 0
    
    for num in nums:
        s += num
        S.append(s)

    prefix_sum = []

    for i in range(M, N+1):
        prefix_sum.append(S[i] - S[i-M])

    max_sum = max(prefix_sum)
    min_sum = min(prefix_sum)

    print(f'#{tc} {max_sum - min_sum}')