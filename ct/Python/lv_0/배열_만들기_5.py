def 배열_만들기_5(intStrs, k, s, l):
    return [int(i_s[s : s+l]) for i_s in intStrs if int(i_s[s : s+l]) > k]