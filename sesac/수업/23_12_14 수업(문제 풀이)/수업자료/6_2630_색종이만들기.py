import sys
input = sys.stdin.readline

def divide_conqure(r, c, n):
    global white, blue

    color = paper[r][c]                                 # 왼쪽 위의 색깔을 기준으로 하고

    for i in range(r, r + n):                           # 탐색 시작
        for j in range(c, c + n):

            if color != paper[i][j]:                    # 다른 색을 발견했다면

                divide_conqure(r, c, n//2)              # 4등분하여 재귀
                divide_conqure(r, c+n//2, n//2)
                divide_conqure(r+n//2, c, n//2)
                divide_conqure(r+n//2, c+n//2, n//2)

                return
    
    if color == 0:                                      # 모두 같은 경우 집계
        white += 1
    else:
        blue += 1

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0

divide_conqure(0, 0, N)

print(white)
print(blue)