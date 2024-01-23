# https://school.programmers.co.kr/learn/courses/30/lessons/120868

# 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
# 삼각형의 두 변의 길이가 담긴 배열 sides이 매개변수로 주어집니다. 나머지 한 변이 될 수 있는 정수의 개수를 return하도록 solution 함수를 완성해주세요.

def solution(sides):
    # 배열 안에 가장 긴 선분이 있는 경우
    long = max(sides)
    short = min(sides)
    ans = [num for num in range(long - short + 1, long + 1)]

    # 배열 안에 없는 선분이 제일 긴 경우
    ans += [num for num in range(long + 1, short + long)]
    return len(set(ans))

def solution_2(sides):
    long = max(sides)
    short = min(sides)
    ans = [num for num in range(long - short + 1, long + 1)] + [num for num in range(long + 1, short + long)]
    return len(set(ans))

print(solution([1, 2])) # result = 1
print(solution_2([3, 6])) # result = 5
print(solution([11, 7])) # result = 13