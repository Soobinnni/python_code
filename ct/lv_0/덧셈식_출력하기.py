# 덧셈식 출력하기
# 문제 설명
# 두 정수 a, b가 주어질 때 다음과 같은 형태의 계산식을 출력하는 코드를 작성해 보세요.

# a + b = c
# 제한사항
# 1 ≤ a, b ≤ 100
# 입출력 예
# 입력 #1

# 4 5
# 출력 #1

# 4 + 5 = 9

def check_num(num):
    is_validate = 1 <= num <= 100
    return is_validate
    
def 덧셈식_출력하기():
    a, b = map(int, input().strip().split(' '))

    if check_num(a) and check_num(b):
        print(f"{a} + {b} = {a + b}")