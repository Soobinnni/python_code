# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

# 배운 점: pop사용하기
for test_case in range(1, int(input())+1):
    n = int(input())
    nums = sorted(list(map(int, input().split())))
    res = []
    for i, num in enumerate(nums[::-1][:5]):
        res.append(num)
        res.append(nums[i])

    print(f"#{test_case}", *res)

for tc in range(1, int(input()) + 1):

    N = int(input())
    nums = sorted(list(map(int, input().split())))

    ans = []

    for i in range(10):  # 정렬 결과 10개까지 출력

        if i % 2 == 1:  # 홀수번째에는
            ans.append(nums.pop(0))  # 앞에서 꺼내서 붙이고

        elif i % 2 == 0:  # 짝수번째에는
            ans.append(nums.pop())  # 뒤에서 꺼내서 붙인다

    print(f'#{tc}', end=' ')
    print(*ans)