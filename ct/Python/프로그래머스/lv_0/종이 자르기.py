# https://school.programmers.co.kr/learn/courses/30/lessons/120922

def solution(M, N):
    return (M * N) -1

def get_cut_cnt_dfs(width, height):
    width, height = min(width, height), max(width, height)

    if width == 1 and height == 1:
        return 0

    return 1 + get_cut_cnt_dfs(width, height//2) + get_cut_cnt_dfs(width, height-height//2)

def solution_2(M, N):
    return get_cut_cnt_dfs(M, N)


print(solution(2, 2)) # result = 3
print(solution(2, 5)) # result = 9
print(solution(1, 1)) # result = 0