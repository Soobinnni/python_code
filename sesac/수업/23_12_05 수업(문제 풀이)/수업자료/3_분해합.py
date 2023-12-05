import sys
input = sys.stdin.readline

N = int(input())
start = max(1, N - (9 * len(str(N))))
ans = 0

for num in range(start, N+1):
    disassemble_sum = num + sum(map(int, str(num)))

    if disassemble_sum == N:
        ans = num
        break

print(ans)