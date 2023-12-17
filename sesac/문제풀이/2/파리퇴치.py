t = int(input())

for test_case in range(1, t+1):
    n, m = map(int, input().split())
    count_flies = [list(map(int, input().split())) for _ in range(n)]

    ans = -1
    flapper = 0

    for i in range(n-m+1):
        flapper = 0
        for j in range(n-m+1):
            flapper = sum(count_flies[x][y] for x in range(i, i+m) for y in range(j, j+m))
            if ans < flapper: ans = flapper

    print(f'#{test_case} {ans}')