# https://www.acmicpc.net/problem/15654

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

# combinations 모듈 사용
from itertools import permutations
for comb in permutations(arr, M):
    print(*comb)


# 직접 구현하기
sel = [0] * M
check = [0] * N

def perms(depth):
    if depth == M:
        print(*sel)
        return

    for i in range(N):
        if not check[i]:
            check[i] = 1
            sel[depth] = arr[i]
            perms(depth + 1)
            check[i] = 0
perms(0)