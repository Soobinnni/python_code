

def find_third_wheel(ns): # 내 답
    rs = [num for num in set(ns) if ns.count(num) == 1] # ns는 정수 리스트
    print(rs) # 개수는 print(len(rs))

def bit_find_third_wheel(ns):
    answer = 0
    for num in ns:
        answer ^= num
    print(answer)
nums = [3,2,4,2, 4, 1,3]
nums2 = [77, 26, 34, 25, 17, 5, 8, 5, 17, 34, 25, 26, 77]
bit_find_third_wheel(nums2)


