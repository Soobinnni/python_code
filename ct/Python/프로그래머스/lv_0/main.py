from 문자열_출력하기 import 문자열_출력하기, 문자열_출력하기2, 문자열_출력하기3
from a와_b_출력하기 import a와_b_출력하기
from 문자열_반복해서_출력하기 import 문자열_반복해서_출력하기
from 대소문자_바꿔서_출력하기 import 대소문자_바꿔서_출력하기
from 특수문자_출력하기 import 특수문자_출력하기
from 덧셈식_출력하기 import 덧셈식_출력하기
from 문자열_붙여서_출력하기 import 문자열_붙여서_출력하기
from 문자열_돌리기 import 문자열_돌리기
from 홀짝_구분하기 import 홀짝_구분하기
from 문자열_겹쳐쓰기 import 문자열_겹쳐쓰기
from 문자열_섞기 import 문자열_섞기
from 문자_리스트를_문자열로_변환하기 import 문자_리스트를_문자열로_변환하기
from 문자열_곱하기 import 문자열_곱하기
from 더_크게_합치기 import 더_크게_합치기
from 두_수의_연산값_비교하기 import 두_수의_연산값_비교하기
from A_강조하기 import A_강조하기
from n의_배수 import n의_배수
from 공배수 import 공배수
from 홀짝에_따라_다른_값_반환하기 import 홀짝에_따라_다른_값_반환하기, num_list_한줄로쓰기_홀짝에_따라_다른_값_반환하기, 남의_답_한줄로쓰기_홀짝에_따라_다른_값_반환하기
from 조건_문자열 import 조건_문자열 
from flag에_따라_다른_값_반환하기 import flag에_따라_다른_값_반환하기 
from 코드_처리하기 import 코드_처리하기
from 등차수열의_특정한_항만_더하기 import 등차수열의_특정한_항만_더하기
from 주사위_게임_2 import 주사위_게임_2
from 원소들의_곱과_합 import 원소들의_곱과_합
from 이어_붙인_수 import 이어_붙인_수
from 마지막_두_원소 import 마지막_두_원소
from 수_조작하기_1 import 수_조작하기_1
from 수_조작하기_2 import 수_조작하기_2
from 평행 import 평행
from 최빈값_구하기 import 최빈값_구하기
from 수열과_구간_쿼리_3 import 수열과_구간_쿼리_3
from 수열과_구간_쿼리_2 import 수열과_구간_쿼리_2
from 수열과_구간_쿼리_4 import 수열과_구간_쿼리_4
from 배열_만들기_2 import 배열_만들기_2
from 주사위_게임_3 import 주사위_게임_3
from 카운트_업 import 카운트_업
from 콜라츠_수열_만들기 import 콜라츠_수열_만들기
from 배열_만들기_4 import 배열_만들기_4
from 간단한_논리_연산 import 간단한_논리_연산
from 글자_이어_붙여_문자열_만들기 import 글자_이어_붙여_문자열_만들기
from 구로_나눈_나머지 import 구로_나눈_나머지
from 문자열_여러_번_뒤집기 import 문자열_여러_번_뒤집기
from 배열_만들기_5 import 배열_만들기_5
from 부분_문자열_이어_붙여_문자열_만들기 import 부분_문자열_이어_붙여_문자열_만들기
from 문자열의_뒤의_n글자 import 문자열의_뒤의_n글자
from 접미사_배열 import 접미사_배열
from 접미사인지_확인하기 import 접미사인지_확인하기
from 문자열의_앞의_n글자 import 문자열의_앞의_n글자
from 접두사인지_확인하기 import 접두사인지_확인하기
from 문자열_뒤집기 import 문자열_뒤집기
from 정수를_나선형으로_배치하기 import 정수를_나선형으로_배치하기
from 겹치는_선분의_길이 import 겹치는_선분의_길이
from 분수의_덧셈 import 분수의_덧셈

def def_naming(file_name):
    return "".join(("" if i == 0 else "_") + a for i, a in enumerate(file_name.split()))
    
def add_from_import_sts_and_call_func_sts(func_name):
    main_file_path = "./ct/Python/lv_0/main.py"
    with open(main_file_path, 'r', encoding="UTF-8") as file:
        lines = file.readlines()
    last_import_index = 0
    for i, line in enumerate(lines):
        if line.startswith("from ") and " import " in line:
            last_import_index = i
    lines.insert(last_import_index + 1, f"from {func_name} import {func_name}" + '\n')
    lines.append(f"\n\t{func_name}()")

    with open(main_file_path, 'w', encoding="UTF-8") as file:
        file.writelines(lines)

def create_new_file(file_name):
    file_name_func_name = def_naming(file_name)

    f = open(f"./ct/Python/lv_0/{file_name_func_name}.py", 'w', encoding="UTF-8")
    f.write(f"""def {file_name_func_name}():\n\tpass""")
    f.close()
    
    add_from_import_sts_and_call_func_sts(file_name_func_name)

if __name__ == "__main__" :
    # 2023/11/8
	    # 접두사인지_확인하기("banana", "ban")
    
    # 2023/11/11
		# 문자열_뒤집기("Progra21Sremm3", 6, 12)
    
    # 2023/11/14
        # 문자열_출력하기3()
        # a와_b_출력하기()
        # 문자열_반복해서_출력하기()
        # 대소문자_바꿔서_출력하기()
        # 특수문자_출력하기()
        # 덧셈식_출력하기()

    # 2023/11/15
        # 문자열_붙여서_출력하기()
        # 문자열_돌리기()
        # 홀짝_구분하기()
        # 문자열_겹쳐쓰기("hahahahahahahahha", "youretoslow", 4)
        # 문자열_섞기("str", "str2")
        # 문자_리스트를_문자열로_변환하기(['a', 'b', 'c'])
        # 문자열_곱하기('abc')
        # 더_크게_합치기(1, 1)
        # 두_수의_연산값_비교하기(1, 2)
        # A_강조하기("PrOgRaMmErS")
        # n의_배수(98, 2)
        # 공배수(60, 2, 3)
        # print(남의_답_한줄로쓰기_홀짝에_따라_다른_값_반환하기(6))
        # 조건_문자열("<", "=", 41, 81)
        # flag에_따라_다른_값_반환하기(-4, 7, True)
        # 코드_처리하기("abc1abc1abc")
    
    #2023/11/18
        # 등차수열의_특정한_항만_더하기(3, 4, [True, False, False, True, True])

    #2023/11/19
        # 주사위_게임_2(2, 6, 1)

    #2023/11/20
        # 원소들의_곱과_합([3, 4, 5, 2, 1])

    #2023/11/21
        # 이어_붙인_수([3, 4, 5, 2, 1])
        # 마지막_두_원소([2, 1, 6])
    
    #2023/11/22
        # 수_조작하기_1(0, "wsdawsdassw")

    #2023/11/24
        # 수_조작하기_2([0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1])

    #2023/11/25
        # 평행([[1, 4], [9, 2], [3, 8], [11, 6]])
        # 최빈값_구하기([1, 2, 3, 3, 3, 4])
        # 수열과_구간_쿼리_3([0, 1, 2, 3, 4], [[0, 3],[1, 2],[1, 4]])
        # 수열과_구간_쿼리_2([0, 1, 2, 4, 3], [[0, 4, 2],[0, 3, 2],[0, 2, 2]])
	
    #2023/11/26
        # 수열과_구간_쿼리_4([0, 1, 2, 4, 3], [[0, 4, 1],[0, 3, 2],[0, 3, 3]])
	
    #2023/11/27
        # 주사위_게임_3(4,1,4,4)
    
    #2023/11/28
        # 카운트_업(3, 8)
        # 콜라츠_수열_만들기(10)
        # 배열_만들기_4([1, 4, 2, 5, 3])

    #2023/11/29
        # 간단한_논리_연산(True, True, True, False)
        # 글자_이어_붙여_문자열_만들기("cvsgiorszzzmrpaqpe", [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7])
        # 구로_나눈_나머지("123")
	
    #2023/11/30
        # 문자열_여러_번_뒤집기("remrgorpsam", [[2, 3], [0, 7], [5, 9], [6, 10]])
        # 배열_만들기_5(["0123456789","9876543210","9999999999999"], 50000, 5, 5)
        # 부분_문자열_이어_붙여_문자열_만들기(["progressive", "hamburger", "hammer", "ahocorasick"], [[0, 4], [1, 2], [3, 5], [7, 7]])
        # 문자열의_뒤의_n글자("ProgrammerS123", 11)
        # 접미사_배열("banana")

    #2023/12/2
	    # 접미사인지_확인하기("banana", "ana")

    #2023/12/13
        # 배열_만들기(5, 555)

    #2023/12/14
        # 옹알이1(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"])

    #2023/12/14
    # 	정수를_나선형으로_배치하기(3)
	# 겹치는_선분의_길이([[0, 1], [2, 5], [3, 9]])

    create_new_file("")