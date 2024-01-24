# https://school.programmers.co.kr/learn/courses/30/lessons/120885

def solution(bin1, bin2):
    # return bin(int(bin1, 2) + int(bin2, 2))[2:]
    return format(int(bin1, 2) + int(bin2, 2), 'b')

print(solution("10", "11")) # result = 101
print(solution("1001", "1111")) # result = 11000