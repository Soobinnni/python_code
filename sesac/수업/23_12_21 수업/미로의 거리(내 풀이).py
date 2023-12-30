# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

# 0은 통로, 1은 벽, 2는 출발, 3은 도착
# 경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를, 경로가 없는 경우 0을 출력한다.

from collections import deque
for test_case in range(1, int(input())+1):
    N = int(input())
    # maze = [list(map(int, input())) for _ in range(N)]
    maze = []
    dist = []
    ans = 0
    # cnt = 0
    for _ in range(N):
        maze.append(list(map(int, input())))
        dist.append([0] * N)

    # 시작점과 끝점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                initial_r, initial_c = i, j
            if maze[i][j] == 3:
                final_r, final_c = i, j

    # 최단 거리 계산
    Q = deque([(initial_r, initial_c)])

    while Q:
        r, c = Q.popleft()
        if r == final_r and c == final_c:
            ans = dist[r][c] - 1
            break
        for dr, dc in [(-1, 0),(1, 0),(0, -1),(0, 1)]:
            nr, nc = r + dr, c + dc
            # 범위 안, 통로 0, visited가 아니라면
            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != 1 and dist[nr][nc] == 0:
                Q.append((nr,nc))
                dist[nr][nc] = dist[r][c] + 1

    print(f"#{test_case} {ans}")

# output
#1 5
#2 5
#3 0

# input
"""
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000
"""