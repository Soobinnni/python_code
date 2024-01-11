# https://www.acmicpc.net/problem/15655

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

# 모듈 사용
from itertools import combinations
for comb in combinations(arr, M):
    print(*comb)
    
# 직접 구현
sel = [0] * M
def comb(idx, sidx):
    if sidx == M:
        print(*sel)
        return
    if idx == N:
        return

    sel[sidx] = arr[idx]
    comb(idx + 1, sidx + 1)
    comb(idx + 1, sidx)

comb(0, 0)