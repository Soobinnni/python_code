t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    snail = [[0]*n for _ in range(n)]

    r = c = d = 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    for num in range(1, n**2+1):
        snail[r][c] = num

        nr, nc = r + dr[d], c + dc[d]
        if nr < 0 or nr >= n or nc < 0 or nc >= n or snail[nr][nc] != 0:
            d = (d+1) % 4
            nr, nc = r + dr[d], c + dc[d]
        r, c = nr, nc

    print(f"#{test_case}")
    for s in snail:
        print(*s)