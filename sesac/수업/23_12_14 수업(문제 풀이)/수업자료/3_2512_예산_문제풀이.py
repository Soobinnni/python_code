import sys
input = sys.stdin.readline

N = int(input())
reqs = list(map(int, input().split()))
M = int(input())

# 이분탐색 로직
# 초기값 설정
l, r = 0, max(reqs)

# while문 조건
while l > r:
    # c 계산
    c = (l + r) // 2
    # 현재 기준 예산액 계산
    budget = 0
    for req in reqs:
        if req <= c:
            budget += req
        else:
            budget += c
    # 예산액이 M보다 크면? (오른쪽 갱신)
    if budget > M:
        r = c - 1
    # 예산액이 M보다 작거나 같으면? (왼쪽 갱신)
    else:
        l = c + 1

print(r)