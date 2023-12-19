dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    # 틀짜기
    board = [[0 for _ in range(M+2)] for _ in range(N+2)]
    # 입력받아 갖다붙이기
    for i in range(1, N+1):
        board[i][1:M+1] = map(int, input().split())

    ans = 0

    for r in range(1, N+1):
        for c in range(1, M+1):
            tmp = board[r][c]

            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                tmp += board[nr][nc]

            ans = max(ans, tmp)

    print(f'#{tc} {ans}')