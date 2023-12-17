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