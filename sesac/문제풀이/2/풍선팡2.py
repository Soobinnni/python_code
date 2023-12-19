def case_1():
    t = int(input())

    for test_case in range(1, t+1):
        n, m = map(int, input().split())
        balloons = [list(map(int, input().split())) for _ in range(n)]
        ans = -1
        pollen = 0

        for i in range(n):
            for j in range(m):
                pollen = balloons[i][j]
                if i > 0:
                    pollen += balloons[i-1][j]
                if i < n-1:
                    pollen += balloons[i+1][j]
                if j > 0 :
                    pollen += balloons[i][j-1]
                if j < m-1:
                    pollen += balloons[i][j+1]

                if ans < pollen: ans = pollen

        print(f'#{test_case} {ans}')

def case_2():
    t = int(input())

    for test_case in range(1, t+1):
        n, m = map(int, input().split())

        # 틀짜기
        balloons = [[0 for _ in range(m+2)] for _ in range(n+2)]

        # 입력받아 갖다 붙이기
        for i in range(1, n+1):
            balloons[i][1:m+1] = map(int, input().split())

        ans = -1
        pollen = 0

        for j in range(1, n+1):
            for k in range(1, m+1):
                pollen = balloons[j][k]
                for x,y in [(j-1, k), (j+1, k), (j, k-1), (j, k+1)]:
                    pollen += balloons[x][y]

                if ans < pollen: ans = pollen

        print(f'#{test_case} {ans}')