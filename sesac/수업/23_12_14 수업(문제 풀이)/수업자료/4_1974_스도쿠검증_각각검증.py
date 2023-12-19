def row_check():
    for r in range(9):
        check = set()
        for c in range(9):
            check.add(sudoku[r][c])

        if len(check) < 9:
            return 0
    return 1

def column_check():
    for c in range(9):
        check = set()
        for r in range(9):
            check.add(sudoku[r][c])

        if len(check) < 9:
            return 0
    return 1

def grid_check():
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            check = set(sudoku[y][x] for y in range(r, r+3) for x in range(c, c+3))

            if len(check) < 9:
                return 0
    return 1

for tc in range(1, int(input())+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    ans = row_check() and column_check() and grid_check()

    print(f'#{tc} {ans}')