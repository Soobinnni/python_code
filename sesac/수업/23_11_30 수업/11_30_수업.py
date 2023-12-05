# input은 input값을 모두 str 타입으로 받음
# num = input('입력 값을 입력해주세요.\n')
#
# print(num, type(num))
#
# # map과 같은 원리
# nums = input().split()
# for i in range(len(nums)):
#     nums[i] = int(nums[i])
#
# print(nums)
#
# # map을 통해 int함수를 적용해줌 : map함수가 int함수로 mutable한 데이터를 맵핑해줌
# nums2 = list(map(int, input().split()))
# print(nums2)
#
# c = list(reversed(nums2))
# print(nums2, c)
#
# a = [1, 2, 3, 4]
# a[1:2] = [5, 5, 5]
#
# a = [1, 2, 3, 4]
# a[1:2] = [5, 5, 5]

# a -> [1, 5, 5, 5, 3, 4]

# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do
# 입력
# 3
# 5
# 477162 658880 751280 927930 297191
# 5
# 565469 851600 460874 148692 111090
# 10
# 784386 279993 982220 996285 614710 992232 195265 359810 919192 158175

# 출력
# #1 630739
# #2 740510
# #3 838110

# 분석
# 3
# ------------test case가 3번------------
# 5
# 477162 658880 751280 927930 297191
# ---------------------------------------
# 5
# 565469 851600 460874 148692 111090
# ---------------------------------------
# 10
# 784386 279993 982220 996285 614710 992232 195265 359810 919192 158175

# 1. 우선 3을 받아본다 -> 테스트 케이스 숫자!
T = int(input()) # 테스트 케이스가 총 3개다.
str = T + "\n"
for test_case in range(1, (T+1)):
    # 출력이 #1 ~ #3을 요구하므로
    # #1 630739
    # #2 740510
    # #3 838110

    N = int(input()) # list의 len을 받는다
    li = list(map(int, input().split()))

    f'#{test_case} {max(li)-min(li)}'