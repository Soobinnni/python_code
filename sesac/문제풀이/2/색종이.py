# https://www.acmicpc.net/problem/2563

# copy문제 조심


# 색종이 = 100 * 100
# 색종이의 수
# 둘째 줄부터 한 줄에 하나씩 색종이를 붙인 위치
    # 첫 번째 자연수는 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리
    # 두 번째 자연수는 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리
# 색종이의 수는 100 이하이며, 색종이가 도화지 밖으로 나가는 경우는 없다

# 색종이가 붙은 검은 영역의 넓이를 출력

# 3
# 3 7
# 15 7
# 5 2

import time
now = time.time()
paper = [[0] * 100 for _ in range(100)]
# N = int(input())
# color_papers = [list(map(int, input().split())) for _ in range(N)]
#
#
# for m, n in color_papers:
#     for i in range(10):
#         for j in range(10):
#             paper[m+i][n+j] = 1

for _ in range(int(input())):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1

print(sum(sum(p) for p in paper))
fin = time.time()
print(fin-now)


#================================
# import numpy as np
# import time
#
# now = time.time()
# paper = np.zeros((100,100))
#
# for _ in range(int(input())):
#     x, y = map(int, input().split())
#     paper[x : x+10, y : y+10] = 1
#
# fin = time.time()
# print(fin-now)
# print(int(np.sum(paper)))