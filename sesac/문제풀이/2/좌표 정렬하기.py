# https://www.acmicpc.net/problem/11650

for c in sorted(list(tuple(map(int, input().split())) for _ in range(int(input())))): print(*c)