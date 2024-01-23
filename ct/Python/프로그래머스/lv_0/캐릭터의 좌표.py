# https://school.programmers.co.kr/learn/courses/30/lessons/120861

def solution(keyinput, board):
    move = {
        'up': (0,1),
        'down': (0,-1),
        'left': (-1,0),
        'right': (1,0)
    }
    x, y = 0, 0

    for key in keyinput:
        dx, dy = move[key]
        nx, ny = x +  dx, y + dy
        if (nx > board[0] // 2) or (nx < -(board[0] // 2)) or (ny > board[1] // 2) or (ny < -(board[1] // 2)):
            continue
        x, y = nx, ny
    return [x, y]

solution(["left", "right", "up", "right", "right"], [11, 11])
solution(["down", "down", "down", "down", "down"], [7, 9])