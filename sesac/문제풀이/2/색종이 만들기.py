N = int(input())
colored_papers = [list(map(int, input().split())) for _ in range(N)]
color_count = {
    0 : 0, # 흰
    1 : 0  # 파
}

def devide_conqure(r, c, n):
    color = colored_papers[r][c]

    for y in range(r, r+n):
        for x in range(c, c+n):
            if colored_papers[y][x] != color:
                n = n // 2
                devide_conqure(r, c, n)
                devide_conqure(r, c+n, n)
                devide_conqure(r+n, c, n)
                devide_conqure(r+n, c+n, n)
                return
    color_count[color] += 1

devide_conqure(0, 0, N)

for result in color_count.values(): print(result)