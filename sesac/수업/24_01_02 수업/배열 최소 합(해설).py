# https://swexpertacademy.com/main/learn/course/subjectDetail.do?subjectId=AWOVIc7KqfQDFAWg#

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]
    answer = 99999999999999999
    ans = 99999999999999999
    check = [0]*N

    def perm(depth, acc):
        global answer

        # 리소스 낭비: 재귀를 돌기 전에 조건문으로 재귀함수를 call할 지 조건을 거는 것이 좋다.
        if acc >= answer:  # 백트래킹
            return  # 이미 해당 뎁스에서 구해진 최솟값보다 크거나 같으면 의미 x

        if depth == N:  # 최후 뎁스 도달 시,
            if answer > acc:
                answer = acc  # 최솟값 갱신 시도
            return  # 아니라도 일단 리턴

        for i in range(N):
            # 여기서 누적합이 최소인지 검사하는 if문을 추가하는 것이 더 바람직!(시간 초과 문제)
            if not check[i]:
                check[i] = 1
                perm(depth + 1, acc + nums[depth][i])
                check[i] = 0

    # 내 풀이
    def find_min_num(depth, acc):  # acc는 누적합
        global ans
        if depth == N:
            if ans > acc:
                ans = acc
            return

        for i in range(N):
            tmp_num = acc + nums[depth][i]
            if not check[i] and (tmp_num < ans):
                check[i] = 1
                find_min_num(depth + 1, tmp_num)
                check[i] = 0

    perm(0, 0)

    print('#{} {}'.format(tc, answer))

"""
3
3
2 1 2
5 8 5
7 2 2
3
9 4 7
8 6 5
5 3 7
5
5 2 1 1 9
3 3 8 3 1
9 2 8 8 6
1 5 7 8 3
5 5 4 6 8
"""
#1 8
#2 14
#3 9