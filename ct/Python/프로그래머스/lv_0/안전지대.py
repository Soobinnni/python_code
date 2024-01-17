# https://school.programmers.co.kr/learn/courses/30/lessons/120866

test_case1 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]] # result = 16
test_case2 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]	# result = 13
test_case3 = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]] # result = 0

def solution(board):
    N = len(board)
    for x in range(N):
        for y in range(N):
            if board[x][y] == 1:
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        if board[nx][ny] == 1: continue
                        board[nx][ny] = 2

    return sum(b.count(0) for b in board)

print(solution(test_case1))
print(solution(test_case2))
print(solution(test_case3))