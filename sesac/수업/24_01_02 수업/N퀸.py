# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GKs06AU0DFAXB
# https://www.acmicpc.net/problem/9663
"""
    한 행과 한 열에 하나의 퀸만 존재해야 함.
    대각선 체크가 관건
"""
# ==============================visited 활용하기=====================================

"""
# visited 확인
def queens_road(r, c, eraser = False):
    # 아래
    for j in range(r, N):
        visited[j][c] += 1 if eraser else -1

    # 아래 왼쪽 대각선
    for k in range(1, N):
        nr, nc = r + k, c - k
        if 0 <= nr < N and 0 <= nc < N:
            visited[nr][nc] += 1 if eraser else -1
        else:
            break

    # 아래 오른쪽 대각선
    for l in range(1, N):
        nr, nc = r + l, c + l
        if 0 <= nr < N and 0 <= nc < N:
            visited[nr][nc] += 1 if eraser else -1
        else:
            break

# 순열 재귀
def deploy_queens(depth):
    global cnt
    if depth == N:
        cnt += 1
        return

    for i in range(N):
        if visited[depth][i] == 0:
            queens_road(depth, i)
            deploy_queens(depth + 1)
            queens_road(depth, i, True) # 방문을 지운다.

for test_case in range(1, int(input())+1):
    N = int(input())
    visited = [[0] * N for _ in range(N)]
    cnt = 0

    deploy_queens(0)
    print(f"{test_case} {cnt}")
"""

# ==============================열 번호 활용하기========================================
"""
def deploy_queens(depth):
    global cnt
    if depth == N:
        cnt += 1
        return

    for i in range(N):
        column_arr[depth] = i
        for check_depth in range(depth):
            # 열 검사
            if column_arr[check_depth] == i: break
            # 대각선 검사
            if (abs(column_arr[check_depth]  - i)) == (depth - check_depth): break
        else:
            deploy_queens(depth + 1)

for test_case in range(1, int(input()) + 1):
    N = int(input())
    column_arr = [0] * N
    cnt = 0

    deploy_queens(0)
    print(f"#{test_case} {cnt}")
"""

# ==============================이차원 배열 특징 활용하기=================================
"""
def assign_values_to_check_array(check_idx, ld_idx, rd_idx, value):
    check[check_idx] = value
    ld[ld_idx] = value
    rd[rd_idx] = value
def deploy_queens(depth):
    global cnt
    if depth == N:
        cnt += 1
        return

    for i in range(N):
        if (not check[i]) and (not ld[depth - i]) and (not rd[depth + i]):
            assign_values_to_check_array(i, depth - i, depth + i, 1)
            deploy_queens(depth + 1)
            assign_values_to_check_array(i, depth - i, depth + i, 0)

for test_case in range(1, int(input()) + 1):
    N = int(input())
    diagonal_len = (N *  2) - 1

    check = [0] * N
    ld = [0] * diagonal_len
    rd = [0] * diagonal_len
    cnt = 0

    deploy_queens(0)
    print(f"#{test_case} {cnt}")

"""

# ===============================================================================
"""
- 입력
3
1
2
8

- 출력
#1 1
#2 0
#3 92
"""