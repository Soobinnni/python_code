def check(board):
    for line in board:
        if len(set(line)) < 9:
            return 0
    
    return 1

for tc in range(1, int(input())+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    sudoku2 = list(zip(*sudoku))    # sudoku2: 전치(열 우선)

    sudoku3 = []                    # sudoku3: 칸별로

    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
           sudoku3.append([sudoku[i][j] for i in range(x, x+3) for j in range(y, y+3)])

    ans = check(sudoku) and check(sudoku2) and check(sudoku3)

    print(f'#{tc} {ans}')