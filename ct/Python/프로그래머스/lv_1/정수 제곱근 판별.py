def solution(n):
    ans = -1
    num = 1
    while num <= (n // 2 + 1):
        if num ** 2 == n:
            ans = (num + 1) ** 2
            break

        num += 1
    return ans

# 다른 사람의 정답: ** (1/2)는 제곱근
def nextSqure(n):
    sqrt = n ** (1/2)
    return (sqrt + 1) ** 2 if sqrt % 1 == 0 else -1

print(solution(121)) # result = 144
print(nextSqure(3)) # result = -1