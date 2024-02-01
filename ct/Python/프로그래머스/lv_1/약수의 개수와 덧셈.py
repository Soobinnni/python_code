# https://school.programmers.co.kr/learn/courses/30/lessons/77884

# 내 답
def get_measure_num(n):
    if n == 1: return 1
    measure_cnt = 2  # 기본적으로 1과 자기 자신
    for i in range(2, n // 2 + 1):
        if n % i == 0: measure_cnt += 1
    return measure_cnt


def solution(left, right):
    ans = 0
    for num in range(left, right + 1):
        if get_measure_num(num) % 2 == 0:
            ans += num
        else:
            ans -= num

    return ans
# 다른 사람의 답
# 힌트: 제곱의 약수는 홀수 개.

def other_solution(left, right):
    ans = 0
    for num in range(left, right+1):
        if (int(num**0.5)) == (num**0.5):
            ans -=num
        else:
            ans += num
    return ans

print(solution(13, 17)) # result = 43
print(solution(24, 27)) # result = 52
print(other_solution(13, 17)) # result = 43
print(other_solution(24, 27)) # result = 52