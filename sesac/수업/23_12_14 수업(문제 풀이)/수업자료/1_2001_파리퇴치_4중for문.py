for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for r in range(N - M + 1):
        for c in range(N - M + 1):
            tmp = 0
            for y in range(r, r+M):
                for x in range(c, c+M):
                    tmp += board[y][x]
            ans = max(tmp, ans)

    print(f"#{tc} {ans}")