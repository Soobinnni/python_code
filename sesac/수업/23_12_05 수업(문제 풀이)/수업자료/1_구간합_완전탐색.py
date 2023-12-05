for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    prefix_sum = []

    for i in range(N-M+1):
        prefix_sum.append(sum(nums[i:i+M]))

    max_num = max(prefix_sum)
    min_num = min(prefix_sum)

    print(f'#{tc} {max_num - min_num}')