# https://www.acmicpc.net/problem/1012

# 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한(상하좌우) 다른 배추로 이동할 수 있어,
# 그 배추들 역시 해충으로부터 보호받을 수 있다.

# 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)
# 세로길이 N(1 ≤ N ≤ 50),
# 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다.

# ==  1 군집의 개수를 세기!
def dfs(r, c):
    stack = [(r, c)]
    while stack:
        r, c = stack.pop()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and board[nr][nc] == 1:
                stack.append((nr, nc))
                board[nr][nc] = 0

for _ in range(int(input())):
    N, M, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        x, y = map(int, input().split())
        board[x][y] = 1

    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                board[i][j] = 0
                dfs(i, j)
                cnt += 1

    print(cnt)