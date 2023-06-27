# 입력 값이 홀수인지 짝수인지 구분하는 프로그램

input_num = int(input('숫자를 입력 :\n>>>'))

if input_num % 2 == 0 :
    print(f'{input_num}은 짝수입니다!')
else :
    print(f'{input_num}은 홀수입니다!')

# 번외 : 문자열에 포함하느냐로 물을 수 있다.
if str(input_num) in "246810" :
    print(f'{input_num}은 짝수입니다!')

if str(input_num) in "1357911" :
    print(f'{input_num}은 홀수입니다!')