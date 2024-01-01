# https://www.acmicpc.net/problem/4396


N = int(input())
mineboard = [list(map(str, input())) for _ in range(N)]
player_board = [list(map(str, input())) for _ in range(N)]

mine_location = [] # 지뢰 위치 저장
player_select_location = [] # 플레이어 선택 위치 저장
padding_mineboard = [[0] * (N+2) for _ in range(N+2)] # index error 방지
d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)] # 상하좌우대각선

for i in range(1, N+1): # 패딩 배열 저장, 지뢰 위치 저장, 플레이어 선택 위치 저장
    for j in range(1, N+1):
        if mineboard[i-1][j-1] == '*':
            mine_location.append((i-1, j-1))
            padding_mineboard[i][j] = 1
        if player_board[i-1][j-1] == 'x':
            player_select_location.append((i-1, j-1))

for x, y in player_select_location:
    if padding_mineboard[x + 1][y + 1] == 1:  # 지뢰를 밟으면
        for m, n in mine_location:
            player_board[m][n] = '*'
    else:
        mine_num = 0
        for dr, dc in d:
            nr = x + dr + 1
            nc = y + dc + 1
            mine_num += padding_mineboard[nr][nc]
        player_board[x][y] = str(mine_num)

for p in player_board: print(''.join(p))