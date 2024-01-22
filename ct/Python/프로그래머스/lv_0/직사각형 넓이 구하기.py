# https://school.programmers.co.kr/learn/courses/30/lessons/120860

def solution(dots):
    x1, y1 = dots.pop()
    h, w = 0, 0
    for x2, y2 in dots:
        if x1 == x2: h = abs(y1 - y2)
        if y1 == y2: w = abs(x1 - x2)
        if w * h: return w * h

print(solution([[1, 1], [2, 1], [2, 2], [1, 2]])) # result = 1
print(solution([[-1, -1], [1, 1], [1, -1], [-1, 1]])) # result = 4