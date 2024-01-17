# 문제 설명
# 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.

# 제한사항
# 0 < array의 길이 < 100
# 0 ≤ array의 원소 < 1000
# 입출력 예
# array	result
# [1, 2, 3, 3, 3, 4]	3
# [1, 1, 2, 2]	-1
# [1]	1
# 입출력 예 설명
# 입출력 예 #1

# [1, 2, 3, 3, 3, 4]에서 1은 1개 2는 1개 3은 3개 4는 1개로 최빈값은 3입니다.
# 입출력 예 #2

# [1, 1, 2, 2]에서 1은 2개 2는 2개로 최빈값이 1, 2입니다. 최빈값이 여러 개이므로 -1을 return 합니다.
# 입출력 예 #3

# [1]에는 1만 있으므로 최빈값은 1입니다.

def 최빈값_구하기(array):
    # 1) array의 num을 key로, num의 count를 value로 저장
    d_dict = {}
    for num in array:
        if num not in d_dict:
            d_dict[num] = 1
        else:
            d_dict[num] += 1

    # 2) value(num의 count) 중 max 고르기
    max_count = max(d_dict.values())
    check_count = 0
    # 3) 2의 max카운트
    for num, count in d_dict:
        if max_count == count:
            check_count += 0
            max_num = num

    return max_num if check_count == 1 else -1    


def 남의_답_최빈값_구하기(array):

    # while문 안의 remove로, 요소의 길이가 계속 차감 -> list길이가 0이 되면 while 종료
    while len(array) != 0:

        # set함수로 중복 요소가 제거된 
        for i, a in enumerate(set(array)):
            # remove함수는 제거하거자 하는 특정 요소가 list에 여럿일 때 
            # index가 제일 최신의 특정 요소만 제거(ex : [1, 2, 1, 3].remove(1) -> [2, 1, 3])
            array.remove(a)

        # python for문의 마지막 순회에 사용된 변수(구체적으로 할당된 변수의 값)는
        # for문을 빠져나온 뒤에도 사용 가능.
        # 만일, 마지막으로 제거된 a의 index가 0이라면, 마지막으로 제거되지 않고 남아진 
        # list의 요소가 최빈값이.(만일 마지막까지도 len(array)가 2라면 마지막 순회의 i는 1이므로
        # return a를 하지 못하고 while을 빠져나오고, return -1을 하게 됨)
        if i == 0: return a
    return -1