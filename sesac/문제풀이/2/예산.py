"""
1. 상한액은 -> 총 예산 / 지방의 예산 요청 수
2. 상한액을 넘지 않으면 그대로 줄 수 있음
3. 상한액을 넘으면 상한액을 주거나, 남은 예산을 가지고 그대로 줄 수 있음 
"""
# def cal_budgets(l, h):
#     # l이 r보다 크면 r을 반환하고 재귀 종룔
#     if l>h:
#         return h
#     # 중간 값 계산
#     mid = (l+h) // 2
#
#     # 현재 기준 예산액 계산
#     budget = 0
#     for r in request_budgets:
#         budget += mid if r >= mid else r
#
#     # 예상 예산을 기준으로 조건 재귀
#     if budget < total_budget:
#         return cal_budgets(mid+1, h)
#     elif budget > total_budget:
#         return cal_budgets(l, mid-1)
#
# n = int(input())
# request_budgets = list(map(int, input().split()))
# total_budget = int(input())
#
# ans = cal_budgets(0, max(request_budgets))
#
# print(ans)

n = int(input())
reqs = list(map(int, input().split()))
M = int(input())

l, r = 0, max(reqs)

while l > r:
    c = (l + r) // 2

    budget = 0
    for req in reqs:
        if req <= c:
            budget += req
        else:
            budget += c

    if budget > M:
        r = c - 1
    else:
        l = c + 1

print(r)