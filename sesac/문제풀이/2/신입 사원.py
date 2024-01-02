# https://www.acmicpc.net/problem/1946

for _ in range(int(input())):
    N = int(input())
    info = [tuple(map(int, input().split())) for _ in range(N)]
    info.sort()

    cnt = 0
    standard = N + 1

    for i in range(N):
        if info[i][1] < standard:
            cnt += 1
            standard = info[i][1]

    print(cnt)