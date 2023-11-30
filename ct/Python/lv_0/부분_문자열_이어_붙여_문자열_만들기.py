def 부분_문자열_이어_붙여_문자열_만들기(my_strings, parts):
    return ''.join(my_strings[i][a:(b+1)] for i, (a, b) in enumerate(parts))