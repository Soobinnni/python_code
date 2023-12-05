for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    prefix_tmp = sum(nums[:M])
    prefix_sum = [prefix_tmp]

    for i in range(N-M):
        prefix_tmp += nums[i+M] - nums[i]
        prefix_sum.append(prefix_tmp)

    max_num = max(prefix_sum)
    min_num = min(prefix_sum)

    print(f'#{tc} {max_num - min_num}')