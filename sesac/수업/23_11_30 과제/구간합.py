T = int(input())

for test_case in range(1, T+1):
    count, integral = map(int, input().split())
    nums = [int(i) for i in input().split()]
    sum_arr = []
    for i in range(count-integral+1):
        sum_arr.append(sum(nums[i : i+integral]))
    result = max(sum_arr) - min(sum_arr)
    print(f'#{test_case} {result}')