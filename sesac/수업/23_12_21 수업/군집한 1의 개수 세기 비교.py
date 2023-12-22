from collections import deque

# [문제]
# N * N 크기의 배열이 주어졌을 때 1의 개수는 몇 개인지 세어보기(dfs를 이용해서)
# 하나의 시작 1로부터 붙어져 있는 연속된 1의 개수 세어보기 => 2, 13이 답이 된다.

# [입력]
"""
7
0000011
0000000
0011100
0010111
0110010
0011100
0000000
"""

def DFS(r, c):
    global cnt
    cnt += 1
    matrix[r][c] = 0

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 > nr or N <= nr or 0 > nc or N <= nc: continue
        if matrix[nr][nc] == 0: continue

        DFS(nr, nc)


def BFS(r, c):
    Q = deque()
    Q.append((r, c))
    dist[r][c] = 1

    while Q:
        cur_r, cur_c = Q.popleft()
        for k in range(4):
            nr = cur_r + dr[k]
            nc = cur_c + dc[k]

            if 0 > nr or N <= nr or 0 > nc or N <= nc: continue
            if matrix[nr][nc] != 1 or dist[nr][nc] != 0: continue

            Q.append((nr, nc))
            dist[nr][nc] = dist[cur_r][cur_c] + 1


N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]

cnt = 0  # for DFS
dist = [[0] * N for _ in range(N)]  # for BFS

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(N):
    for j in range(N):
        # DFS
        if matrix[i][j] == 1:
            cnt = 0
            DFS(i, j)
            print(cnt)

        # BFS
        if matrix[i][j] == 1 and dist[i][j] == 0: BFS(i, j)

for d in dist:
    print(*d)