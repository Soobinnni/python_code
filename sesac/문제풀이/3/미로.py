# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVIc7KqfQDFAWg#

for test_case in range(1, int(input())+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    ans = 0

    # 시작점, 끝점
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                i_r, i_c = i, j
            # if maze[i][j] == 3:
            #     f_r, f_c = i, j

    Q = [(i_r, i_c)]

    # while Q:
    #     r, c = Q.pop()
    #
    #     maze[r][c] = 1
    #
    #     for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    #         nr, nc = r + dr, c + dc
    #         if nr == f_r and nc == f_c:
    #             ans = 1
    #             Q.clear()
    #             break
    #         if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != 1:
    #             Q.append((nr, nc))

    while Q:
        r, c = Q.pop()
        if maze[r][c] == 3:
            ans = 1
            break

        maze[r][c] = 1

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] != 1: Q.append((nr, nc))

    print(f"#{test_case} {ans}")