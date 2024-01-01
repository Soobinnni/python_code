# https://www.acmicpc.net/problem/4396


N = int(input())
mineboard = [list(map(str, input())) for _ in range(N)]
player_board = [list(map(str, input())) for _ in range(N)]

mine_location = [] # 지뢰 위치 저장
padding_mineboard = [[0] * (N+2) for _ in range(N+2)] # index error 방지
d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)] # 상하좌우대각선

for i in range(1, N+1): # 패딩 배열 저장, 지뢰 위치 저장
    for j in range(1, N+1):
        if mineboard[i-1][j-1] == '*':
            mine_location.append((i-1, j-1))
            padding_mineboard[i][j] = 1

for r in range(N):
    for c in range(N):
        if player_board[r][c] == 'x':
            if padding_mineboard[r+1][c+1] == 1: # 지뢰를 밟으면
                for x, y in mine_location:
                    player_board[x][y] = '*'
            else:
                mine_num = 0
                for dr, dc in d:
                    nr = r + dr + 1
                    nc = c + dc + 1
                    mine_num += padding_mineboard[nr][nc]
                player_board[r][c] = str(mine_num)

for p in player_board: print(''.join(p))