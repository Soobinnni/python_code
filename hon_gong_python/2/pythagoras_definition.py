# 밑변과 높이를 입력하면 빗변의 길이를 구하는 프로그램

# 입력
base = float(input('밑변의 길이를 입력해주세요 : '))
height = float(input('높이의 길이를 입력해주세요 : '))
# 처리 x ** (1/n)

hypotenuse =  ((base ** 2) + (height ** 2)) ** (1/2)

# 출력
print(f"빗변의 길이는 {hypotenuse}입니다.")