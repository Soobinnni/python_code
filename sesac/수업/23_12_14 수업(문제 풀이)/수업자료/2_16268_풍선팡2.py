dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    for r in range(N):
        for c in range(M):
            tmp = board[r][c]

            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]

                if 0 <= nr < N and 0 <= nc < M:
                    tmp += board[nr][nc]

            ans = max(ans, tmp)

    print(f'#{tc} {ans}')