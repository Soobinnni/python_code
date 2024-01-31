def solution(x, n):
    if x == 0 : return [0] * n
    plus_integral = 1 if x > 0 else -1
    return [num for num in range(x, (x * n)+plus_integral, x)]

def solution_2(x, n):
    return [x + i * x for i in range(n)]

print(solution(2, 5))
print(solution(4, 3))
print(solution(-4, 2))