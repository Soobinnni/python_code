# https://school.programmers.co.kr/learn/courses/30/lessons/120894/solution_groups?language=python3

def solution(numbers):
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    nums_dict = dict(zip(nums, range(0,10)))
    for num in nums:
        numbers = numbers.replace(num, str(nums_dict[num]))
    return int(numbers)

def solution_2(numbers):
    for num, en in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(en, str(num))

    return int(numbers)

print(solution_2("onetwothreefourfivesixseveneightnine")) # result = 123456789
print(solution("onefourzerosixseven")) # result = 14067