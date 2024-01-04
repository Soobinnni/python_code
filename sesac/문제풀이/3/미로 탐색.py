# https://www.acmicpc.net/problem/2178

# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸
# (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수

from collections import deque

def first():
    N, M  = map(int, input().split())
    maze = [list(map(int, input())) for _ in range(N)]

    Q = deque([(0, 0)])
    dis = [[0]*M for _ in range(N)]
    dis[0][0] = 1

    while Q:
        r, c = Q.popleft()

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] == 1 and dis[nr][nc] == 0:
                Q.append((nr, nc))
                dis[nr][nc] = dis[r][c] + 1


    print(dis[N-1][M-1])

def second():
    N, M = map(int, input().split())
    maze = [list(map(int, input())) for _ in range(N)]

    Q = deque([(0, 0)])

    while Q:
        r, c = Q.popleft()

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] == 1:
                Q.append((nr, nc))
                maze[nr][nc] = maze[r][c] + 1

    print(maze[N - 1][M - 1])

second()