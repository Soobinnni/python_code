def check_duplicate(idx):
    r = (idx // 3) * 3
    c = (idx % 3 ) * 3
    num_list = [sudoku[r][c]]

    for dr, dc in [(0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]:
        num = sudoku[r+dr][c+dc]
        if num in num_list: return False
        num_list.append(num)
    return True

for test_case in range(1, int(input())+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    column_sudoku = list(map(list, zip(*sudoku)))
    ans = 0

    for i in range(9):
        if len(set(sudoku[i])) != 9 or len(set(column_sudoku[i])) != 9: break
        if not check_duplicate(i): break
    else: ans = 1

    print(f"#{test_case} {ans}")