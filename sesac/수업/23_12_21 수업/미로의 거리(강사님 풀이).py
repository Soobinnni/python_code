from collections import deque

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                initial_r, initial_c = i, j
            elif arr[i][j] == 3:
                final_r, final_c = i, j

    Q = deque([[initial_r, initial_c]])
    visited = set()
    visited.add((initial_r, initial_c))
    dist = -2 # 처음과 끝점을 뺴고 계산하기 위해
    flag = False

    while Q:
        size = len(Q) # while문을 도는 동안 좌표들이 Q안에 들어갈텐데,
                      # 돌 때마다 Q 안에는 인접한 좌표들이 들어있음
                      # 돌고 난 뒤 Q안에 끝점이 있는 지 검사하고, 있으면 flag를 True로하고
                      # 그때의 dist를 반환한다.
        for _ in range(size):
            r, c = Q.popleft()
            if r == final_r and c == final_c:
                flag = True
                Q.clear()
                break

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 1 and (nr, nc) not in visited:
                    Q.append([nr, nc])
                    visited.add((nr, nc))

        # 등고선 개수만큼만 +1이므로 형제 좌표를 다 돈 후 dist에 1을 더해준다(안 그렇게 하면 등고선 개수만큼 더해짐).
        dist += 1


    if flag:
        print(f'#{tc} {dist}')
    else:
        print(f'#{tc} {0}')