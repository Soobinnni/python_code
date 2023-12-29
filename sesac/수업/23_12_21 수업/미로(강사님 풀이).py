for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]

    # 먼저 시작점과 끝점을 미리 찾아놓는다.
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                initial_r, initial_c = i, j
            elif arr[i][j] == 3:
                final_r, final_c = i, j

    stack = [[initial_r, initial_c]]
    visited = set()
    visited.add((initial_r, initial_c))
    answer = 0

    while stack:
        r, c = stack.pop()
        if r == final_r and c == final_c: # 모두 만족이므로 and
            answer = 1
            break

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            # map 안에 있고 / 0으로 가는 길목이 있고 / 방문하지 않았다면
            if 0 <= nr < 16 and 0 <= nc < 16 and arr[nr][nc] != 1 and (nr, nc) not in visited:
                visited.add((nr, nc))
                stack.append([nr, nc])

    print(f'#{tc} {answer}')