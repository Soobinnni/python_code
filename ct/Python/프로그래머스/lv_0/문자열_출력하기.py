# 문제 설명
# 문자열 str이 주어질 때, str을 출력하는 코드를 작성해 보세요.

# 제한사항
# 1 ≤ str의 길이 ≤ 1,000,000
# str에는 공백이 없으며, 첫째 줄에 한 줄로만 주어집니다.
# 입출력 예
# 입력 #1

# HelloWorld!
# 출력 #1

# HelloWorld!

# 내가 작성한 코드
def 문자열_출력하기():
    str = input()
    len_str = len(str)
    if 1 <= len_str <=1000000:
        strgr = str.strip().split(" ")
        oneline_str = ""
        for s in strgr:
            oneline_str += s
        print(oneline_str)

# 새로 개선 : 불필요한 for문 대신, join() 내장 함수 사용
def 문자열_출력하기2():
    str = input()
    len_str = len(str)
    if 1<=len_str<=1000000:
        strgr = str.strip().split(" ")
        oneline_str = "".join(strgr)
        print(oneline_str)

# 새로 개선 : 공백은 안 됨
def 문자열_출력하기3():
    str = input()
    len_str = len(str)
    if 1<=len_str<=1000000 and len(str.strip()) != 0:
        strgr = str.strip().split(" ")
        oneline_str = "".join(strgr)
        print(oneline_str)