T = int(input())

for test_case in range(1, T+1):
    count, integral = map(int, input().split())
    nums = [int(i) for i in input().split()]
    sum_arr = []
    # indexerror가 나지 않도록, 범위 잘 지정하기
    for i in range(count-integral+1):
        sum_arr.append(sum(nums[i : i+integral]))
    result = max(sum_arr) - min(sum_arr)
    print(f'#{test_case} {result}')
    
    
# 브루트포스
# 슬라이딩윈도우
# 누적합