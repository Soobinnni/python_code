# https://www.acmicpc.net/problem/7576

# 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳(상하좌우)에 있는 익지 않은 토마토들은
# 익은 토마토의 영향을 받아 익게 된다

# 상자의 크기를 나타내는 두 정수 M,N
# 둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보
# 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.
# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸

# 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성

# 출력
# 1. 최소 일수
# 2. 저장될 때부터 모든 토마토가 익어있는 상태이면 0
# 3. 토마토가 모두 익지는 못하는 상황이면 -1

from collections import deque

M, N = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(N)]
dis = -1 # 출발점 제외

Q = deque()
# 익은 토마토 담기
for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 1:
            Q.append((i, j))
while Q:
    size = len(Q)
    for _ in range(size):
        r, c = Q.popleft()

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and tomatoes[nr][nc] not in (1, -1):
                Q.append((nr, nc))
                tomatoes[nr][nc] = 1 # 기록(visited)
    dis += 1

for t in tomatoes:
    if 0 in t:
        dis = -1
        break

print(dis)