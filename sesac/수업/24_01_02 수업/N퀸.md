# N퀸
## 첫 번째 방법
- `원시적으로 푼다.`
- 체스판과 똑같은 N * N 2차원의 visited배열을 만들고 방문체크
- 아래 방향만 방문 체크 하면 된다(depth로 탐색하므로): 아래(column), 아래 왼쪽 대각선, 아래 오른쪽 대각선
  > - 백트래킹 == visited 확인의 로직을 거쳐 N퀸의 경우의 수를 구한다.
### 코드
```python
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
```
---

## 두 번째 방법
- `퀸의 열 번호`를 적는 1차원 배열의 자료구조를 활용한다.
  > - 1차 백트래킹 == 기준 원소의 인덱스보다 이전 인덱스들의 원소의 값이 기준 원소의 값과 겹치지 않도록 한다.
  > - 2차 백트래킹 == (퀸의 열 번호의 인덱스 차) == (퀸의 열 번호의 원소 값의 차이) 라면, 대각선에 위치한 것이므로 백트래킹 조건으로 추가한다. 
## 코드
```python
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
```
---

## 세 번째 방법
- `2차원 배열의 특징`을 활용한다.
  > - 백트래킹 == 이차원 배열의 좌, 우대각선에 위치한 좌표들의 특징을 이용한 배열로 조건을 건다. 
  >   - 두 배열의 길이는 (N * 2) - 1 
  >   - `ld = [0, 1, 2, 3, ..., (N-1), -(N-1), -(N-2), -(N-3), ..., -1]`
  >   - `rd = [0, 1, 2, 3, ..., ((N-1) * 2)]`
### 코드
  ```python
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
      cnt = 0
  
      check = [0] * N
      ld = [0] * diagonal_len
      rd = [0] * diagonal_len
  
      deploy_queens(0)
      print(f"#{test_case} {cnt}")
  ```