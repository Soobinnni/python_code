# a와 b 출력하기
# 문제 설명
# 정수 a와 b가 주어집니다. 각 수를 입력받아 입출력 예와 같은 형식으로 출력하는 코드를 작성해 보세요.

# 제한사항
# -100,000 ≤ a, b ≤ 100,000
# 입출력 예
# 입력 #1

# 4 5
# 출력 #1

# a = 4
# b = 5

def a와_b_출력하기():
    def check_validate_num(num):
        is_validate = -100000 <= num <= 100000
        return is_validate

    a, b = map(int, input().strip().split(' '))

    if check_validate_num(a) and check_validate_num(b):
        print(f"a = {a}\nb = {b}")