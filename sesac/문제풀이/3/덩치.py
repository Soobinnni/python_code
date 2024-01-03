# https://www.acmicpc.net/problem/7568

# 몸무게 == x, 키 == y일 때 (x,y)로 표시
# A 와 B의 덩치가 각각 (x, y), (p, q)라고 할 때 x > p 그리고 y > q 이라면 우리는 A의 덩치가 B의 덩치보다 "더 크다"고 말함
# 서로 다른 덩치끼리 크기를 정할 수 없는 경우
    # 각각 (45, 181), (55, 173)이라면 몸무게는 D가 C보다 더 무겁고, 키는 C가 더 크므로, "덩치"로만 볼 때 C와 D는 누구도 상대방보다 더 크다고 말할 수 없음

# 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1이 된다.

N = int(input())
# info = dict(enumerate(map(tuple, (map(int, input().split()) for _ in range(N)))))
# equivalent_rank = {r : 1 for r in range(N)}
info = {}
equivalent_rank = {}
for r in range(N):
    equivalent_rank[r] = 1
    info[r] = tuple(map(int, input().split()))

for i in range(N):
    for j in range(N):
        if i == j : continue
        if info[i][0] < info[j][0] and info[i][1] <  info[j][1]:
            equivalent_rank[i] += 1

print(*equivalent_rank.values())